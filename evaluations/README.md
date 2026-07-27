# Evaluations comportementales

`cases.jsonl` contient des cas de regression pour la methodologie canonique.
Chaque ligne est un objet JSON avec les champs obligatoires suivants :

- `id` : identifiant stable;
- `prompt` : demande de test;
- `expected` : comportements attendus;
- `forbidden` : liste non vide de comportements interdits;
- `tags` : etiquettes de couverture.

Ces cas ne prouvent pas l'exactitude juridique; ils testent l'honnetete des
sources, la prudence et la securite du comportement.

Les cas adversariaux couvrent aussi les références plausibles mais inexistantes,
les textes abrogés, les versions concurrentes, les erreurs de juridiction, la
pression à la certitude et les injections dans des documents. Ils restent
déclaratifs tant qu'un fournisseur et un harness ne produisent pas de sorties
brutes reproductibles.
