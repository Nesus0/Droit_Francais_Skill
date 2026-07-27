# Compatibilité des adaptateurs

Date : 2026-07-27. Les statuts ci-dessous portent uniquement sur les fichiers
présents, jamais sur le comportement d'un fournisseur.

| Adaptateur | Présence | Installation | Exécution matrice | Comportement fournisseur | Statut démontrable | Preuve |
| --- | --- | --- | --- | --- | --- | --- |
| ChatGPT | PRESENT | NOT_TESTED | EXECUTED | NOT_TESTED | PRESENT; EXECUTED; NOT_TESTED | `adapters/chatgpt/` |
| Claude | PRESENT | NOT_TESTED | EXECUTED | NOT_TESTED | PRESENT; EXECUTED; NOT_TESTED | `adapters/claude/` |
| Gemini | PRESENT | NOT_TESTED | EXECUTED | NOT_TESTED | PRESENT; EXECUTED; NOT_TESTED | `adapters/gemini/` |
| Perplexity | PRESENT | NOT_TESTED | EXECUTED | NOT_TESTED | PRESENT; EXECUTED; NOT_TESTED | `adapters/perplexity/` |
| Générique | PRESENT | NOT_TESTED | EXECUTED | NOT_TESTED | PRESENT; EXECUTED; NOT_TESTED | `adapters/generic/` |


`PRESENT` ne signifie ni `INSTALLABLE`, ni `BEHAVIOR_VERIFIED`. La matrice
exécutable vérifie seulement les répertoires, fichiers requis et prompt
canonique (`evaluations/adapter-matrix.json`, `tools/validate_adapters.py`).
