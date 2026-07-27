# Confidentialité et données sensibles

Le dépôt ne collecte pas de dossiers; le risque apparaît lorsque son contenu est
utilisé dans un produit IA. La qualification RGPD, AI Act, secret professionnel
ou conformité contractuelle exige une validation spécialisée.

| Donnée | Risque | Exécution locale | API distante | Interface grand public |
| --- | --- | --- | --- | --- |
| Dossiers clients | faits, identité, stratégie et pièces exposés | périmètre machine à contrôler | fournisseur, rétention et transferts à vérifier | réutilisation, historique et contrôle organisationnel incertains |
| Données RH | santé, salaire, discipline, identifiants | chiffrage et accès local à contrôler | minimisation, DPA, région et logs à vérifier | éviter par défaut; ne pas coller de dossier brut |
| Pièces contentieuses | secret de procédure, preuves, métadonnées | journalisation et sauvegardes locales | conservation et sous-traitants à vérifier | risque accru de partage ou d'entraînement selon service |
| Données médicales | données sensibles et risque de réidentification | pseudonymisation avant traitement | base légale, chiffrement et transferts à vérifier | ne pas utiliser sans cadre approuvé |
| Secrets d'affaires | stratégie, contrats, code, prix | contrôle d'accès local | confidentialité contractuelle et rétention à vérifier | interface non dédiée au secret d'affaires |
| Secret professionnel | obligations déontologiques spécifiques | environnement isolé requis | fournisseur et sous-traitants à qualifier | validation professionnelle indispensable |

## Règles minimales

- minimiser et pseudonymiser avant envoi;
- retirer identifiants, adresses, numéros de dossier et pièces inutiles;
- ne jamais fournir clés, tokens ou cookies;
- vérifier conservation, entraînement, région, chiffrement, accès, suppression et
  contrat du fournisseur;
- séparer local, API distante et interface grand public dans les journaux;
- obtenir l'accord du responsable de traitement, du client ou du professionnel
  compétent lorsque nécessaire.

`docs/scope-and-safety.md`, `SECURITY.md` et les cas `personal-data`/
`pseudonymized-case` prescrivent la minimisation, mais ne prouvent pas un
contrôle technique chez un fournisseur.

## Audit de publication

| ID | Catégorie | Sévérité | Emplacement | Preuve | Correction | Statut |
| --- | --- | --- | --- | --- | --- | --- |
| PAC-001 | Métadonnées Git | BLOCKER initial, corrigé | baseline, tags et pages de commit publiques | l'historique initial utilisait des métadonnées non autorisées, masquées dans ce rapport | reconstruire une racine propre, supprimer refs/releases/runs puis vérifier l'état public; demander une purge GitHub si des objets restent accessibles | correction à vérifier après push; rétention GitHub hors contrôle local |
| PAC-002 | Futurs commits | INFO | configuration Git locale | identité locale remplacée par `Nesus0` et adresse GitHub noreply | vérifier après le prochain commit public | corrigé localement |
| PAC-003 | Arbre et archive | INFO | fichiers suivis et archive `v4.1.5` | aucun chemin local, secret, média ou document bureautique suivi détecté | conserver le validateur public en CI | vérifié localement; archive publique contrôlée |
