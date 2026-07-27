# Release readiness

Date de référence : 2026-07-27 (Europe/Paris). La baseline antérieure est
volontairement non identifiée afin de ne pas rendre directement navigable un
objet GitHub en attente de purge.

## Etat

| Controle | Etat | Preuve |
| --- | --- | --- |
| Fichiers essentiels | PASS | `quality.yml` |
| Registre des sources | PASS | `python3 tools/validate_sources.py` |
| Evaluations JSONL | PASS | `python3 tools/validate_evals.py` |
| Syntaxe Python | PASS | `python3 -m py_compile ...` |
| Liens Markdown relatifs | PASS | controle local de l'audit |
| Archive de baseline | PASS | archive publiée `v4.1.5` inspectée avant assainissement |
| Reproductibilité byte-à-byte de l'archive | PASS | `create_archive.py --check-reproducible`, SHA-256 identique deux fois |
| Release GitHub finale | À VÉRIFIER | publier `v4.1.7` depuis l'historique assaini, puis comparer son SHA-256 |
| Licence detectee | PASS | GitHub `cc-by-sa-4.0` |
| Harness LLM | PASS structurel | dry-run des 28 cas; aucun appel fournisseur |
| Tests comportementaux executes | NON VERIFIE | aucune réponse LLM réelle |
| Matrice adaptateurs | PASS structurel | `validate_adapters.py`; fournisseurs non exécutés |
| Fraicheur de chaque source | NON VERIFIE | pas de snapshot ni de champ date |
| Revue juridique de chaque domaine | NON VERIFIE | validation humaine requise |
| Actions epinglees par SHA | PASS limité | SHA complets présents; migration Node 24 à revalider sur GitHub |
| Workflows GitHub de baseline | PASS | Quality Check et Release réussis avant assainissement; les nouveaux runs restent à contrôler |
| Syntaxe YAML locale | PASS limité | Ruby YAML 2.6.10; parseur GitHub Actions non exécuté localement |
| Confidentialité historique | PASS conditionnel | historique racine et tag final contrôlés par `validate_publication.py --include-history`; la purge des objets GitHub non référencés reste dépendante de l'hébergeur |

## Niveaux de maturité

### `GO_WITH_RESERVATIONS` — niveau actuel

- audit statique et contrôles de structure exécutés;
- comportement LLM, adaptateurs et revue juridique humaine non vérifiés;
- limites de sources, fraîcheur et confidentialité visibles.

### `RELEASE_CANDIDATE_WITH_EVIDENCE`

À atteindre uniquement après exécution réelle des tests LLM, conservation des
sorties brutes redigées, résultats reproductibles et premières revues humaines
documentées.

### `PUBLIC_RELEASE_VALIDATED_FOR_SCOPE`

À atteindre uniquement pour des domaines explicitement délimités, après revue
humaine, contrôle de fraîcheur sur le périmètre et tests d'adaptateurs. Les
limites doivent rester publiées.

## Verdict

`GO_WITH_RESERVATIONS`. La release est techniquement publiable comme dépôt de
méthodologie après le contrôle de confidentialité des références publiques. Elle
ne doit pas être présentée comme un service de consultation juridique ou comme
un benchmark de fiabilité modèle.
