# Audit des affirmations publiques

Date de référence : 2026-07-27. Cet audit compare les formulations publiées aux
fichiers du dépôt. Une présence documentaire n'est pas une preuve d'exécution.

| Affirmation | Preuve disponible | Niveau | Limites | Formulation autorisée | À éviter |
| --- | --- | --- | --- | --- | --- |
| « Méthodologie portable » | `SKILL.md`, `core/methodology.md` | vérifié statiquement | aucune intégration runtime | « corpus méthodologique portable » | « compatible partout » |
| « Indépendante des fournisseurs » | `core/` sans SDK ni client | vérifié statiquement | dépend du produit cible | « le noyau ne contient pas de SDK fournisseur » | « même comportement chez tous les fournisseurs » |
| « Parcours vers des sources officielles » | `references/sources.json` | vérifié statiquement | URL non équivalente à consultation | « registre de parcours officiels » | « sources consultées automatiquement » |
| « Évaluations comportementales » | 28 cas JSONL et validateur | présent mais non exécuté | aucun harness LLM | « cas attendus déclaratifs » | « benchmark validé » |
| « Garanties contre les citations inventées » | règles dans `core/system-prompt.md` | présent mais non exécuté | respect par un modèle non démontré | « règles prescrites contre l'invention » | « anti-hallucination garantie » |
| « Couverture jurisprudence » | `JURISPRUDENCE_COVERAGE.md` | partiellement vérifié | plusieurs juridictions sans parcours dédié | « couverture partielle documentée » | « toutes les décisions françaises » |
| « Release publiée » | tag, archive et release `v4.1.5` observés avant assainissement | partiellement vérifié | la release finale doit être contrôlée sur GitHub après publication | « la release indiquée sur GitHub est publiée » | « chaque release est juridiquement validée » |
| « Archive sans caches Python » | workflow `zip --exclude` | présent mais non exécuté sur CI actuelle | contrôle local seulement | « le workflow demande l'exclusion » | « archive CI inspectée » |
| « Licence CC BY-SA 4.0 » | `LICENSE`, `LICENSE.fr.md`, badge README | vérifié statiquement | portée des sources externes distincte | « code/documentation du dépôt sous CC BY-SA 4.0 » | « toutes les données externes sous cette licence » |
| « Profils avocat, RH, CSE… » | fichiers sous `profiles/` | vérifié statiquement | contenu déclaratif, pas conseil juridique | « profils documentaires présents » | « profils validés par des avocats » |
| « Adaptateurs ChatGPT, Claude, Gemini, Perplexity » | `adapters/*` | présent mais non exécuté | installation et comportement non testés | « instructions d'adaptation présentes » | « adaptateurs certifiés » |
| « Qualité CI » | workflow, validateurs et runs GitHub réussis | partiellement vérifié | migrations futures et sécurité fournisseur à surveiller | « contrôles définis et exécutés sur GitHub » | « pipeline sécurisé et exhaustif » |

## Catégories utilisées

- **vérifié statiquement** : constat directement reproductible dans les fichiers;
- **présent mais non exécuté** : procédure ou cas présent sans exécution cible;
- **partiellement vérifié** : preuve limitée à un périmètre ou à une exécution;
- **non vérifié** : preuve actuelle insuffisante;
- **non démontré** : aucune preuve dans le dépôt.

Toute communication doit reprendre la formulation autorisée et le niveau de
preuve. Un badge, un nom de fichier ou un résultat de validateur de schéma ne
doit pas être présenté comme une validation juridique ou comportementale.
