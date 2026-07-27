# Audit de fraîcheur juridique

Date de référence de cet audit : 2026-07-27. La fraîcheur d'aucune règle du
corpus n'est déclarée vérifiée par ce document.

## Risques

- texte modifié, abrogé ou recodifié après une réponse antérieure;
- texte publié mais pas encore entré en vigueur;
- réforme future, décret d'application manquant ou dispositions transitoires;
- convention collective modifiée, étendue ou inapplicable au salarié;
- règle territoriale différente ou instrument européen nécessitant transposition;
- prescription et délais calculés depuis une date factuelle non fournie.

## Contrôle reproductible

1. Fixer `date_reference`, territoire et événement déclencheur.
2. Identifier le texte ou la décision avec une source primaire accessible.
3. Comparer publication, entrée en vigueur, abrogation, modifications et
   version consolidée; relever les textes d'application et transitions.
4. Vérifier l'applicabilité aux faits, à la catégorie de personne et au
   territoire; séparer vigueur et opposabilité.
5. Conserver URL finale, titre, organisme, identifiant, version, date de
   consultation, passage et résultat de contrôle.
6. En cas d'accès ou d'historique manquant, produire `[NON VERIFIE]` et une
   conclusion conditionnelle; ne pas appliquer une réforme future.

## État du dépôt

`core/methodology.md` et `core/system-prompt.md` prescrivent ces étapes, et
les cas `vigour-check`/`future-reform` les représentent. Aucune version
historique, API authentifiée ou revue humaine n'a été exécutée dans ce dépôt; la
fraîcheur reste donc **non démontrée**.
