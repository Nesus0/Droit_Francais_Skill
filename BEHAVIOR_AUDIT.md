# Audit comportemental

## Résultat exécutable

Le dépôt contient 28 cas JSONL et un validateur de structure, mais aucun moteur
LLM, client fournisseur, serveur, fixture d'appel ou adaptateur exécutable. Les
fichiers `adapters/*` sont des instructions de correspondance produit. Il est
donc impossible de produire un taux de réussite ou de comparer ChatGPT, Claude,
Gemini et Perplexity depuis le dépôt seul.

Commandes exécutées le 2026-07-27 :

```text
python3 tools/validate_sources.py                 PASS
python3 tools/validate_evals.py                   PASS
python3 -m py_compile tools/validate_sources.py tools/validate_evals.py PASS
```

## Couverture déclarative

| Famille | Cas présents | État réel |
| --- | --- | --- |
| Sources non vérifiées et inaccessibles | `unverified-source`, `source-inaccessible` | Spécification seulement |
| Temporalité et vigueur | `vigour-check`, `future-reform` | Spécification seulement |
| Hiérarchie des sources | `conflicting-sources` | Spécification seulement |
| Prompt injection | `prompt-injection-source` | Spécification seulement |
| Vie privée et pseudonymisation | `personal-data`, `pseudonymized-case` | Spécification seulement |
| Preuves et sécurité | `litigation-evidence` | Spécification seulement |
| Domaines et territoires | pénal, RH/KALI, CSE, outre-mer, civil | Spécification seulement |
| Cas adversariaux | références inexistantes, textes abrogés, versions concurrentes, mauvaise juridiction, certitude forcée, injection | Spécification seulement |

## Scénarios non prouvés

Les tests demandés sur les faux numéros de pourvoi, mauvaises chambres, dates
erronées, citations tronquées, décisions obsolètes ou cassées, source secondaire
seule et conflits d'adaptateurs n'ont pas de mécanisme d'exécution. Ils doivent
être ajoutés à un harness opt-in qui capture le modèle, le fournisseur, la date,
les sources effectivement ouvertes et une sortie redigée; sans secret dans le
dépôt.

## Constats

- `BEHAVIOR-HIGH-001` : les évaluations ne prouvent pas le comportement réel
  d'un modèle; confiance élevée, correction non réalisée.
- `BEHAVIOR-HIGH-002` : aucune assertion automatisée ne vérifie qu'une citation
  existe ou que le lien mène au passage cité; confiance élevée, correction non
  réalisée.
- `BEHAVIOR-MEDIUM-003` : les adaptateurs décrivent des capacités dépendantes
  du compte et du produit; une comparaison nécessite un protocole externe,
  confiance élevée.

## Verdict comportemental

Le noyau impose textuellement des garde-fous contre les références inventées
(`core/methodology.md:28-35`, `core/system-prompt.md:1-16`), mais leur résistance
en production reste non démontrée. Communication autorisée : « cas attendus
déclaratifs », pas « anti-hallucination prouvée ».
