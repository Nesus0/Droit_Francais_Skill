# Droit Francais Skill

[![Release](https://img.shields.io/github/v/release/Nesus0/Droit_Francais_Skill)](https://github.com/Nesus0/Droit_Francais_Skill/releases)
[![Licence : CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-green.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Qualite](https://github.com/Nesus0/Droit_Francais_Skill/actions/workflows/quality.yml/badge.svg)](https://github.com/Nesus0/Droit_Francais_Skill/actions/workflows/quality.yml)

Version 4.1.8 d'une methodologie portable pour une assistance prudente en
information et recherche juridiques en droit francais.

Ce projet fournit un noyau independant des fournisseurs, des correspondances
documentees, des profils, des parcours vers les sources publiques officielles et
des evaluations comportementales. Il ne promet ni couverture exhaustive et a
jour, ni applicabilite juridique universelle. Les sources et leur applicabilite
doivent etre verifiees au regard des faits et de la date de reference.

## Demarrage rapide

1. Lire `core/methodology.md`.
2. Utiliser `core/system-prompt.md` dans la surface d'instructions du produit,
   lorsqu'elle existe.
3. Fournir le profil applicable et les documents du domaine comme references.
4. Utiliser `references/sources.json` pour orienter la verification vers les
   sources publiques officielles; ce fichier ne prouve pas qu'une source a ete
   consultee.
5. Suivre la correspondance reelle du produit dans `adapters/`.

Le `SKILL.md` racine est une enveloppe portable courte autour du noyau canonique.
Il ne remplace ni ne duplique la methodologie.

## Correspondances d'installation

Pour un chargeur de skills ZIP, utiliser l'archive attachee a une release GitHub
plutot que `Code` > `Download ZIP`: l'archive de release place `SKILL.md` a la
racine.

| Cible | Correspondance reelle |
| --- | --- |
| GPT personnalise ChatGPT | Placer `core/system-prompt.md` dans Instructions; ajouter les documents comme Connaissances lorsque cela est pris en charge. Voir `adapters/chatgpt/`. |
| Claude Code | Copier le repertoire, y compris `SKILL.md`, dans le repertoire de competences Claude choisi. Voir `adapters/claude/`. |
| Gemini | Utiliser le prompt systeme comme instructions personnalisees et joindre les documents uniquement si le produit choisi le permet. |
| Perplexity | Utiliser une surface d'instructions ou un Space pris en charge et joindre les documents lorsque disponible; il n'existe pas d'import universel. |
| Autres produits | Utiliser `adapters/generic/system-prompt.md`. |

Les capacites du fournisseur, la navigation, les Actions, la conservation des
fichiers et la recuperation documentaire varient selon le produit et le compte.
Ne pas affirmer qu'une source ou un fichier a ete consulte s'il n'etait pas
accessible dans l'interaction en cours.

## Profils

| Profil | Troisieme regard |
| --- | --- |
| `profiles/avocat.md` | Partie adverse ou procureur |
| `profiles/juriste-entreprise.md` | Regulateur ou auditeur |
| `profiles/rh.md` | Inspection du travail, URSSAF, conseil de prud'hommes |
| `profiles/cse.md` | DREETS, juge electoral, possible delit d'entrave |
| `profiles/avocat-contentieux.md` | Partie adverse et juge |

Tous les profils preservent les garanties du noyau. Ils interdisent l'assistance
a la fraude ainsi que la destruction, dissimulation, alteration ou fabrication
de preuves.

## Organisation du projet

```text
.
├── SKILL.md                         # Enveloppe portable
├── core/                            # Methodologie et prompt canoniques
├── adapters/                        # Correspondances documentees
├── profiles/                        # Profils operationnels
├── domains/                         # Contenus des domaines juridiques
├── references/                      # Registre des sources et maintenance
├── schemas/                         # Schema du registre
├── evaluations/                     # Cas comportementaux
├── tools/                           # Validateurs sans dependance
├── docs/                            # Perimetre et securite
└── deployment/                      # Guide de deploiement ChatGPT
```

Les contenus de domaine existants restent disponibles et ne constituent pas une
promesse de couverture complete de leur matiere.

## Rapports d'audit

Les preuves, limites et contrôles restants sont détaillés dans
[`AUDIT_ULTIME.md`](AUDIT_ULTIME.md),
[`CLAIMS_AUDIT.md`](CLAIMS_AUDIT.md),
[`CITATION_AUDIT.md`](CITATION_AUDIT.md),
[`LEGAL_FRESHNESS_AUDIT.md`](LEGAL_FRESHNESS_AUDIT.md),
[`ADAPTER_COMPATIBILITY.md`](ADAPTER_COMPATIBILITY.md),
[`AUDIT_REPRODUCIBILITY.md`](AUDIT_REPRODUCIBILITY.md),
[`PRIVACY_AND_CONFIDENTIALITY.md`](PRIVACY_AND_CONFIDENTIALITY.md) et les
rapports de sources, jurisprudence, comportement et menace référencés dans
l'audit ultime.

## Validation

```sh
python3 tools/validate_sources.py
python3 tools/validate_evals.py
python3 tools/validate_adapters.py
python3 -m py_compile tools/validate_sources.py tools/validate_evals.py tools/create_archive.py tools/validate_adapters.py tools/run_llm_evals.py
python3 tools/create_archive.py --check-reproducible
python3 tools/run_llm_evals.py --dry-run --limit 28
```

Le workflow qualite verifie les fichiers essentiels, execute les validateurs,
exerce la campagne LLM sans reseau et produit une archive ZIP deterministe. Les
tags `v*` declenchent la publication d'une release avec l'archive correspondante.

## Perimetre et securite

Lire [`docs/scope-and-safety.md`](docs/scope-and-safety.md) avant tout deploiement
ou usage operationnel. Ne pas utiliser ce projet pour inventer des sources,
contourner des controles licites, ni detruire, dissimuler, alterer ou fabriquer
des preuves.

## Contribution et securite

Les contributions suivent [`CONTRIBUTING.md`](CONTRIBUTING.md). Signaler les
problemes de securite selon [`SECURITY.md`](SECURITY.md). Depot :
https://github.com/Nesus0/Droit_Francais_Skill

## Licence

CC BY-SA 4.0. Voir le texte canonique [`LICENSE`](LICENSE) et sa presentation
francaise [`LICENSE.fr.md`](LICENSE.fr.md).
