# Reproductibilité de l'audit

## Référence

- Dépôt : `Droit_Francais_Skill`
- Commit de départ audité : `c53a6cc5f64889691c5f20fb25562353469da8f3`
- Branche : `main`
- Date : 2026-07-27, Europe/Paris
- Le commit final de cette extension est donné dans le compte rendu; il n'est
  pas poussé vers GitHub.
- Environnement observé : Python 3.14.6, Ruby 2.6.10, macOS Darwin 25.5.0,
  architecture arm64.

## Commandes

```text
python3 tools/validate_sources.py
python3 tools/validate_evals.py
python3 -m py_compile tools/validate_sources.py tools/validate_evals.py
python3 -m py_compile tools/create_archive.py tools/validate_adapters.py tools/run_llm_evals.py
python3 tools/create_archive.py --check-reproducible
python3 tools/validate_adapters.py
python3 tools/validate_publication.py --include-history
python3 tools/run_llm_evals.py --dry-run --limit 28 --output-dir /tmp/droit-francais-audit-run
python3 - <<'PY' ... validation JSON/JSONL ... PY
git diff --check
rg -n -I --hidden '(BEGIN ...|ghp_|sk-|AKIA...)' --glob '!.git/**' .
```

Le générateur déterministe a produit deux fois le SHA-256
`5e6337a6b09da620d830dde0e6dc0cda52962331eff01c0cc686ea49052e3ccd`.

Actions épinglées : `actions/checkout`
`08c6903cd8c0fde910a37f88322edcfb5dd907a8` (v5.0.0),
`actions/setup-python` `e797f83bcb11b83ae66e0230d6156d7c80228e7c` (v6.0.0),
`actions/upload-artifact` `330a01c490aca151604b8cf639adc76d48f6c5d4`
(v5.0.0). La release utilise le CLI GitHub avec `github.token`, pas une action
tierce.

## Résultats et limites

Les validateurs, JSON/JSONL, compilation Python, archive déterministe, matrice
adaptateurs, dry-run des 28 cas, syntaxe YAML via Ruby YAML 2.6.10 et diff
whitespace sont exécutables dans cet environnement. Une archive de release ne
contient que des fichiers suivis par Git, dans un ordre, avec des permissions et
des timestamps normalisés; les sorties `.audit-runs/` ne peuvent donc pas être
distribuées par erreur. Le parseur GitHub Actions
n'a pas été exécuté. Aucun appel LLM réel, adaptateur fournisseur, API
authentifiée, revue juridique ni contrôle de fraîcheur n'a été exécuté.

## Reproduction

Cloner le commit, vérifier `git rev-parse HEAD`, lancer les commandes ci-dessus,
comparer les sorties et noter l'environnement (`python3 --version`, OS,
timezone). Pour un ZIP, exclure `.git`, `*.zip`, `__pycache__` et `*.pyc`,
puis publier le SHA-256 de l'artefact effectivement contrôlé. Le workflow doit
utiliser `tools/create_archive.py`, jamais `zip -r` directement.
