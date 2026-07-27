# Audit de la surface publique GitHub

Contrôle réalisé le 2026-07-27 sur le commit public
`b89ba5fd03da3307272007ec397aa0d399393f3d` et la release `v4.1.5`.

| ID | Catégorie | Sévérité | Preuve publique | Conséquence | Correction | Statut |
| --- | --- | --- | --- | --- | --- | --- |
| GPS-001 | Présentation | INFO | description française, six sujets, README, licence CC-BY-SA détectée et release `v4.1.5` visibles | compréhension publique correcte | aucune | vérifié sur GitHub |
| GPS-002 | Release | INFO | release `v4.1.5`, commit `b89ba5f`, archive et digest SHA-256 visibles | traçabilité de release disponible | aucune | vérifié sur GitHub |
| GPS-003 | CI | MEDIUM | Quality Check réussi mais deux avertissements Node.js 20 visibles | avertissements publics de chaîne CI | actions Node 24, CLI GitHub et CodeQL préparés localement | GitHub à recontrôler après push |
| GPS-004 | Communauté | MEDIUM | GitHub signalait l'absence de modèles d'issues et PR | contribution moins guidée | modèles ajoutés localement | GitHub à recontrôler après push |
| GPS-005 | Confidentialité | BLOCKER initial, corrigé | baseline `b89ba5f`, tags et pages de commit comportaient des métadonnées non autorisées | identité non autorisée exposée dans les références publiques | reconstruction d'une racine propre, suppression des références, releases et runs, puis vérification publique | correction à vérifier après push; purge des objets non référencés dépend de GitHub |

La page Security montre Dependabot alerts, secret scanning et signalement privé
de vulnérabilités activés. CodeQL est configuré localement mais non exécuté à la
date de ce rapport. La page publique montre `Nesus0` comme contributeur, mais cela ne supprime pas
les métadonnées Git brutes. Aucun issue, pull request ou alerte de secret
ouverte n'a été observé; l'absence d'analyse CodeQL ne constitue pas un contrôle
de sécurité positif.
