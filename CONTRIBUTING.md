# Contribuer a Droit Francais Skill

Depot : https://github.com/Nesus0/Droit_Francais_Skill

## Regles de contribution

- Preserver la distinction entre sources primaires verifiees, jurisprudence,
  doctrine, instructions administratives et analyse.
- Ne pas ajouter de references, decisions, citations ou affirmations inventees
  sur l'etat actuel du droit.
- Ne pas supprimer de contenu de domaine sans demande explicite d'un mainteneur.
- Conserver JSON, Python et noms de fichiers en ASCII. Le Markdown francais est
  attendu.
- Ne pas ajouter de donnees personnelles, identifiants, points d'acces prives ou
  contenu source proprietaire.

## Registre et evaluations

Lors d'une modification de `references/sources.json`, conserver les identifiants
uniques stables et ne modifier `schemas/source-registry.schema.json` que si
necessaire. Pour la couverture comportementale, utiliser un objet JSON par ligne
dans `evaluations/cases.jsonl` et conserver les champs documentes dans
`evaluations/README.md`.

Executer avant toute demande d'integration :

```sh
python3 tools/validate_sources.py
python3 tools/validate_evals.py
python3 -m py_compile tools/validate_sources.py tools/validate_evals.py
python3 tools/validate_adapters.py
python3 tools/create_archive.py --check-reproducible
```

## Contenu juridique et contributions IA

Toute modification juridique doit indiquer la source primaire ou officielle,
l'URL, l'organisme, la date de reference, la portee, les limites et le statut de
verification. Une source inaccessible reste `[NON VERIFIE]`. Les contenus
generes par IA exigent une relecture humaine et ne constituent jamais une preuve
de vigueur, de citation ou de conformite.

Ne soumettez pas de dossier, donnees personnelles, donnees RH ou medicales,
secret professionnel, secret d'affaires, cle, jeton ou contenu sans droit de
redistribution. Utilisez le modele d'issue juridique pour signaler une erreur
publique et `SECURITY.md` pour une vulnerabilite.

## Documentation et adaptateurs

Conserver `SKILL.md` comme enveloppe du noyau. Les garanties se modifient dans
`core/methodology.md` et, si le texte du prompt change, dans
`core/system-prompt.md`. La documentation des adaptateurs doit decrire
exactement les correspondances prises en charge et ne pas promettre un format ou
un outil natif indisponible.

## Demandes d'integration

Expliquer le comportement demande, les fichiers concernes, la verification des
sources et les resultats des validateurs. Les criteres de revue, la politique de
versions et les statuts de maturite sont definis dans `GOVERNANCE.md`.
