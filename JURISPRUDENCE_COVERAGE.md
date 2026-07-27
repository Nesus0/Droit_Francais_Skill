# Matrice de couverture jurisprudentielle

Date de référence : 2026-07-27. « Présente » signifie qu'un parcours est
documenté dans le registre; cela ne signifie pas que chaque décision est
accessible, publiée ou vérifiée.

| Ensemble | Parcours officiel dans le dépôt | Recherche/API ou open data | Couverture réellement démontrée | Identifiants / limites |
| --- | --- | --- | --- | --- |
| Cour de cassation | Judilibre | Recherche web; open data Judilibre selon service | Décisions publiées par la Cour | Numéro, chambre, date; pseudonymisation et sélection |
| Cours d'appel | Aucun parcours dédié | Non démontré | Non démontrée | Ne pas inférer depuis Judilibre |
| Tribunaux judiciaires | Aucun parcours dédié | Non démontré | Non démontrée | Publication hétérogène |
| Tribunaux de commerce | Aucun parcours dédié | BODACC candidat, annonces seulement | Décisions non démontrées | Annonce BODACC != jugement |
| Conseils de prud'hommes | Aucun parcours dédié | Non démontré | Non démontrée | Convention collective et publication à distinguer |
| Juridictions pénales | Aucun parcours dédié | Non démontré | Non démontrée | Ne pas promettre exhaustivité |
| Conseil d'État | ArianeWeb | Recherche web | Parcours officiel documenté | Publication sélective; numéro/date à vérifier |
| Cours administratives d'appel | ArianeWeb | Recherche web | Partielle, sans matrice par cour | Couverture exacte non mesurée |
| Tribunaux administratifs | ArianeWeb | Recherche web | Partielle, sans matrice par tribunal | Couverture exacte non mesurée |
| Conseil constitutionnel | Site officiel | Recherche web | Décisions publiées sur site | Numéro/date et effet constitutionnel |
| Tribunal des conflits | Aucun parcours dédié | Non démontré | Non démontrée | À ajouter seulement avec parcours vérifié |
| Juridictions financières | Cour des comptes candidate | Rapports publics | Rapports, pas toutes décisions | Distinguer rapport, arrêt et recommandation |
| CJUE | CURIA | Recherche web; sonde 503 | Parcours référencé, consultation non prouvée | Affaire/ECLI, dispositif et portée |
| CEDH | HUDOC | Recherche web | Parcours référencé | Requête, date, statut et exécution |

## Règles de contrôle d'une décision

Avant de citer une décision, le système doit ouvrir la source officielle, relever
juridiction, formation, date, numéro/ECLI ou identifiant, dispositif et contexte
procédural, puis vérifier cassation/annulation et éventuelles mesures
transitoires. Une décision isolée ne constitue pas une jurisprudence constante.
Les cas `unverified-source`, `source-inaccessible`, `vigour-check` et
`source-hierarchy` imposent ce comportement au niveau déclaratif
(`evaluations/cases.jsonl:1-12`).

## Gaps prioritaires

- Aucun test ne résout réellement un faux numéro, une citation tronquée ou une
  décision cassée : les évaluations sont déclaratives et aucun harness n'exécute
  un modèle.
- Aucun instantané ou jeu de décisions n'est embarqué; la fraîcheur et la
  période couverte doivent être vérifiées à chaque recherche.
- Les juridictions sans parcours dédié doivent être annoncées comme non
  démontrées, jamais comme couvertes par défaut.
