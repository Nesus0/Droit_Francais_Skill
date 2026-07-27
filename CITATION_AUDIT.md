# Audit de fidélité des citations

## Statut

Aucune campagne de fidélité sur un échantillon de décisions ou de réponses de
modèle n'a été exécutée dans ce dépôt. Ce document définit un protocole
reproductible; il ne transforme pas `sources.json` en preuve de consultation.

## Protocole par citation

1. Capturer la demande, la date de référence, le territoire et le profil.
2. Ouvrir l'URL citée; enregistrer URL finale, titre, organisme, date de
   consultation et statut d'accès. Une recherche ou un titre seul ne suffit pas.
3. Relever dans le document l'identifiant, la juridiction, la formation, la date,
   le numéro/ECLI, le dispositif et le passage exact.
4. Comparer l'affirmation avec le passage : `DIRECTE`, `RESUME`, `ANALYSE` ou
   `NON ETABLIE`; conserver la citation et son contexte si nécessaire.
5. Pour un texte, vérifier version, modification, abrogation, entrée en vigueur
   et dispositions transitoires à la date de référence.
6. Pour une décision, vérifier juridiction, chambre, date, numéro, décision
   attaquée, cassation/annulation et portée; ne pas extrapoler une décision isolée.
7. Classer la source : normative, jurisprudence, administrative, doctrine ou
   analyse; ne pas présenter une fiche pratique comme norme.
8. Si inaccessible, écrire `[NON VERIFIE]`, ne pas compléter l'identifiant et
   fournir le parcours officiel et les termes de recherche.

## Fiche de preuve

```yaml
citation_id: CIT-0001
date_reference: 2026-07-27
source_id: legifrance
url_finale: https://...
titre: à relever dans la page
organisme: à relever dans la page
identifiant: article/ECLI/numéro
juridiction: à relever
date_document: à relever
version_et_vigueur: vérifiées ou NON VERIFIEES
passage_exact: citation courte et contexte
relation: DIRECTE|RESUME|ANALYSE|NON ETABLIE
acces: ouvert|restreint|échec
limites: ...
```

Les cas adversariaux de `evaluations/cases.jsonl` couvrent décision inexistante,
article inventé, texte abrogé, date absente, versions contradictoires, mauvaise
juridiction, citation fabriquée et injection. Ils restent déclaratifs tant
qu'un harness ne capture pas les sorties brutes et les sources réellement
ouvertes.
