#!/usr/bin/env python3
"""Opt-in runner for the 28 declarative cases using configurable providers.

Outputs are written below .audit-runs/ by default, which is ignored and must
never be committed. This tool does not claim legal or behavioral validation.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evaluations" / "cases.jsonl"
DEFAULT_OUTPUT = ROOT / ".audit-runs"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_cases(limit: int | None) -> list[dict]:
    cases = [json.loads(line) for line in CASES.read_text(encoding="utf-8").splitlines() if line.strip()]
    return cases[:limit] if limit else cases


def request_payload(provider: str, model: str, system: str, prompt: str) -> tuple[str, dict, dict]:
    if provider == "openai-compatible":
        return (
            "Bearer",
            {"messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}]},
            {},
        )
    if provider == "anthropic":
        return ("x-api-key", {"system": system, "messages": [{"role": "user", "content": prompt}]}, {})
    if provider == "gemini":
        return ("x-goog-api-key", {"contents": [{"parts": [{"text": f"{system}\n\n{prompt}"}]}]}, {})
    raise ValueError(f"unsupported provider: {provider}")


def call_provider(provider: str, base_url: str, model: str, api_key: str, system: str, prompt: str) -> tuple[dict, str]:
    header_name, body, _ = request_payload(provider, model, system, prompt)
    if provider == "openai-compatible":
        url = base_url.rstrip("/") + "/chat/completions"
        body.update({"model": model, "temperature": 0})
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    elif provider == "anthropic":
        url = base_url.rstrip("/") + "/v1/messages"
        body.update({"model": model, "max_tokens": 2048})
        headers = {"x-api-key": api_key, "anthropic-version": "2023-06-01", "Content-Type": "application/json"}
    else:
        url = base_url.rstrip("/") + f"/v1beta/models/{model}:generateContent"
        headers = {"x-goog-api-key": api_key, "Content-Type": "application/json"}
    request = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(request, timeout=120) as response:
        raw = response.read()
    decoded = json.loads(raw)
    if provider == "openai-compatible":
        text = decoded["choices"][0]["message"]["content"]
    elif provider == "anthropic":
        text = "".join(block.get("text", "") for block in decoded.get("content", []))
    else:
        text = decoded["candidates"][0]["content"]["parts"][0]["text"]
    return decoded, text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=("openai-compatible", "anthropic", "gemini"), default="openai-compatible")
    parser.add_argument("--model", default="unset")
    parser.add_argument("--base-url", default="https://api.openai.com/v1")
    parser.add_argument("--api-key-env", default="LLM_API_KEY")
    parser.add_argument("--system-prompt", type=Path, default=ROOT / "core/system-prompt.md")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    cases = load_cases(args.limit)
    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    output = args.output_dir / run_id
    output.mkdir(parents=True, exist_ok=False)
    system = args.system_prompt.read_text(encoding="utf-8")
    metadata = {
        "run_id": run_id,
        "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "provider": args.provider,
        "model": args.model,
        "base_url": args.base_url,
        "api_key_env": args.api_key_env,
        "api_key_present": bool(os.environ.get(args.api_key_env)),
        "cases_sha256": digest(CASES.read_bytes()),
        "system_prompt_sha256": digest(system.encode()),
        "python": sys.version,
        "platform": platform.platform(),
        "dry_run": args.dry_run,
        "raw_outputs_local_only": True,
        "parameters": {"temperature": 0, "timeout_seconds": 120, "max_tokens": 2048},
    }
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    with (output / "prompts.jsonl").open("w", encoding="utf-8") as prompts, (output / "results.jsonl").open("w", encoding="utf-8") as results:
        for case in cases:
            prompts.write(json.dumps({"id": case["id"], "prompt": case["prompt"]}, ensure_ascii=True) + "\n")
            result = {
                "id": case["id"],
                "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                "status": "DRY_RUN" if args.dry_run else "NOT_STARTED",
                "evaluation": "NOT_SCORED",
            }
            if not args.dry_run:
                key = os.environ.get(args.api_key_env)
                if not key:
                    result.update({"status": "ERROR", "error": f"missing environment variable {args.api_key_env}"})
                else:
                    try:
                        raw, text = call_provider(args.provider, args.base_url, args.model, key, system, case["prompt"])
                        (output / "raw").mkdir(exist_ok=True)
                        (output / "raw" / f"{case['id']}.json").write_text(json.dumps(raw, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
                        result.update({"status": "RESPONSE_SAVED_LOCAL_ONLY", "response_sha256": digest(text.encode())})
                    except (OSError, ValueError, KeyError, json.JSONDecodeError, urllib.error.URLError) as exc:
                        result.update({"status": "ERROR", "error_type": type(exc).__name__, "error": str(exc)[:500]})
            results.write(json.dumps(result, ensure_ascii=True) + "\n")
    print(f"run_dir={output}")
    print(f"cases={len(cases)} dry_run={args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
