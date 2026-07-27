# Audit licence et réutilisation

| ID | Catégorie | Sévérité | Preuve | Conséquence | Correction | Statut |
| --- | --- | --- | --- | --- | --- | --- |
| LRA-001 | Licence dépôt | INFO | `LICENSE` et GitHub détectent CC BY-SA 4.0 | licence principale cohérente pour le contenu original du dépôt | aucune | vérifié statiquement et sur GitHub |
| LRA-002 | Sources externes | HIGH | registre d'URL sans corpus embarqué | une URL ne transfère aucun droit de réutilisation | ne pas copier de contenu externe sans vérifier licence, attribution et CGU | règle existante, revue humaine requise |
| LRA-003 | Extraits juridiques | MEDIUM | formats de citation et sources documentés | citation et réutilisation dépendent du document précis | conserver passage minimal, URL, organisme, date et fondement de réutilisation | `HUMAN_REVIEW_REQUIRED` |
| LRA-004 | Marques et fournisseurs | LOW | noms de produits dans adaptateurs | risque de laisser croire à une affiliation | conserver les noms uniquement comme compatibilité documentaire | vérifié statiquement |

La licence couvre les apports originaux au dépôt, pas les sites référencés, les
API, les données, les marques, ni les contenus ajoutés par un contributeur sans
droits. Toute contribution doit fournir attribution, licence de réutilisation,
date de vérification et limites avant fusion.
