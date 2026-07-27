# Audit ultime

## Cadre et verdict

- Date de reference : 2026-07-27 (Europe/Paris, CEST).
- Baseline publique auditée :
  `b89ba5fd03da3307272007ec397aa0d399393f3d` avant assainissement.
- Perimetre : depot Git, workflows, scripts, prompts, profils, domaines,
  registre des sources, evaluations et releases GitHub.
- Verdict : **GO_WITH_RESERVATIONS** après assainissement des références
  publiques; les réserves comportementales et juridiques restent inchangées.

Le depot est publiable comme methodologie open source documentee. Il ne peut pas
etre presente comme un moteur juridique autonome ni comme un systeme dont la
resistance aux hallucinations a ete prouvee en execution : aucun harnais ne lance
les prompts contre un modele ou un adaptateur reel.

## Carte des composants

| Composant | Role reel | Source canonique | Observation |
| --- | --- | --- | --- |
| `SKILL.md` | Enveloppe portable | `core/methodology.md`, `core/system-prompt.md` | Pas de logique d'execution |
| `core/` | Methodologie et prompt | `core/` | Regles de verification, temporalite, limites |
| `profiles/` | Troisieme regard par metier | Fichiers de profil | Contenu declaratif |
| `domains/` | Materiel juridique thematique | Fichiers de domaine | Pas de versionnement par texte source |
| `references/` | Registre, hierarchie et citations | `sources.json` et Markdown | Registre de routage, pas preuve de consultation |
| `evaluations/` | Cas comportementaux JSONL | `cases.jsonl` | Validite de forme seulement |
| `tools/` | Validateurs sans dependances | Scripts Python | Pas de test de runtime LLM |
| `adapters/` | Instructions de mapping produit | Fichiers Markdown | Capacites dependant du compte; aucun adaptateur executable |
| `.github/workflows/` | Validation et packaging | Workflows YAML | Actions majeures épinglées par SHA; runner GitHub hors environnement local |

## Constats

### AUDIT-HIGH-001 — comportement runtime non demontrable

- Preuve : `tools/run_llm_evals.py` prépare une campagne opt-in, mais aucune
  sortie de fournisseur réel ni évaluation sémantique n'est versionnée.
- Consequence : `expected` et `forbidden` sont des exigences declaratives; ils ne
  prouvent pas qu'un fournisseur les respecte.
- Correction : harness opt-in ajouté; exécution fournisseur, revue des sorties
  et tests par fournisseur restent non réalisés.
- Confiance : elevee.

### AUDIT-HIGH-002 — fraicheur des sources non tracee

- Preuve : `references/sources.json:4-20` contient `refresh_policy`, mais aucun
  champ `last_verified_at`, version, hash, test de redirection ou preuve de
  consultation.
- Consequence : le registre decrit un parcours, pas l'etat actuel du droit.
- Correction : non realisee; ajouter une fiche d'audit datee par source, sans
  transformer son existence en verification juridique.
- Confiance : elevee.

### AUDIT-HIGH-003 — couverture jurisprudentielle partielle

- Preuve : cinq routes dediees concernent Judilibre, justice administrative,
  Conseil constitutionnel, CURIA et HUDOC; aucune couverture dediee ne prouve les
  tribunaux judiciaires, cours d'appel, prud'hommes, commerce, Tribunal des
  conflits ou juridictions financieres.
- Consequence : le projet ne doit pas annoncer une couverture jurisprudentielle
  generale.
- Correction : rapport de couverture fourni dans `JURISPRUDENCE_COVERAGE.md`.
- Confiance : elevee.

### AUDIT-BLOCKER-004 — metadonnees personnelles dans l'historique public

- Preuve : les commits et tags publics precedents contiennent un nom civil et
  une adresse personnelle; le controle `validate_publication.py --include-history`
  echoue. Les valeurs ne sont pas reproduites dans ce rapport.
- Consequence : la regle d'identite publique limitee a `Nesus0` n'est pas
  respectee sur GitHub, y compris dans les refs historiques.
- Correction : historique racine reconstruit depuis l'arbre audité; anciennes
  références, releases et runs supprimés, puis publication d'un tag neuf.
  `validate_publication.py --include-history` contrôle les commits et taggers.
  Les objets non référencés et caches GitHub relèvent ensuite de la rétention de
  l'hébergeur et peuvent nécessiter une demande de purge.
- Confiance : élevée. Validation humaine : non pour la réécriture; oui pour une
  éventuelle purge côté hébergeur.

### AUDIT-MEDIUM-001 — actions CI épinglées mais runner non vérifié

- Preuve : les workflows utilisent des SHA complets et des commentaires de
  versions; le runner GitHub n'a pas été exécuté localement.
- Conséquence : la dérive amont est réduite, mais le service GitHub reste à
  vérifier lors d'un prochain run.
- Correction : réalisée dans les deux workflows; validation distante restante.
- Confiance : elevee.

### AUDIT-MEDIUM-002 — lint Markdown limité

- Preuve : `validate_publication.py` contrôle les liens Markdown relatifs,
  fichiers communautaires, secrets usuels et actions épinglées; il ne remplace
  pas un linter typographique Markdown.
- Consequence : les liens Markdown ou incoherences documentaires peuvent casser
  sans bloquer une release.
- Correction : contrôle de liens relatifs intégré à la CI; linter typographique
  non ajouté volontairement pour éviter une dépendance non nécessaire.
- Confiance : elevee.

### AUDIT-MEDIUM-003 — contenu juridique a valider humainement

- Preuve : les domaines contiennent des delais, seuils et formulations generales;
  ils ne portent pas tous une citation datee et verifiee au niveau de chaque
  proposition.
- Consequence : risque de simplification, d'obsolescence ou d'application hors
  contexte.
- Correction : reserve explicite dans le verdict et recommandation de revue par
  domaine avant communication comme reference juridique.
- Confiance : elevee.

## Verifications positives

- Registre JSON valide et identifiants uniques.
- Evaluations JSONL valides, 28 cas, couverture minimale imposee par le validateur.
- Compilation Python valide.
- Liens Markdown relatifs controles : aucun lien casse.
- Aucun secret ou cle privee trouvee dans les fichiers suivis.
- Release `v4.1.5` et workflow Quality observés avec succès avant
  l'assainissement; ils sont remplacés par la publication finale.
- Deux generations locales consecutives via `tools/create_archive.py` ont
  produit le même SHA-256; le contrôle est intégré à la CI.
- Licence CC BY-SA 4.0 reconnue par GitHub; `LICENSE.fr.md` fournit la lecture
  francaise et `LICENSE` le texte canonique.

## Limitations d'execution

Les sondes automatisees ont obtenu `403` sur plusieurs routes Legifrance et DAJ,
`503` sur CURIA et une reinitialisation de connexion sur BOSS. Ces resultats
mesurent l'accessibilite de la sonde au moment de l'audit, pas la validite du
domaine ni la vigueur d'une regle. Les APIs authentifiees, quotas, licences de
reutilisation et versions historiques n'ont pas ete valides sans compte ou
contrat specifique.

La syntaxe YAML a ete parsee localement avec Ruby YAML 2.6.10; PyYAML n'est
pas installe, et le parseur GitHub Actions n'a pas ete execute.

## Formulations publiques autorisees

- « Methodologie open source pour une assistance prudente en information et
  recherche juridiques en droit francais. »
- « Le registre indique des parcours officiels; il ne prouve pas qu'une source a
  ete consultee. »
- « Les evaluations definissent des comportements attendus; elles ne constituent
  pas encore un benchmark multi-modele execute. »

## Formulations a eviter

- « Exactitude juridique garantie. »
- « Toutes les decisions francaises sont couvertes. »
- « L'assistant verifie automatiquement chaque citation. »
- « Remplace un avocat ou un juriste. »

## Verdict final

**GO_WITH_RESERVATIONS** pour la publication open source de la méthodologie,
après assainissement contrôlé de l'historique public. Utilisation expérimentale
uniquement : une validation humaine par domaine et une campagne multi-fournisseurs
restent requises avant toute promesse de comportement ou de couverture juridique.

Rapports complémentaires : `SOURCE_AUDIT.md`, `SOURCE_CANDIDATES.md`,
`JURISPRUDENCE_COVERAGE.md`, `BEHAVIOR_AUDIT.md`, `CLAIMS_AUDIT.md`,
`CITATION_AUDIT.md`, `LEGAL_FRESHNESS_AUDIT.md`, `ADAPTER_COMPATIBILITY.md`,
`AUDIT_REPRODUCIBILITY.md`, `PRIVACY_AND_CONFIDENTIALITY.md` et
`droit-francais-skill-v4-threat-model.md`.
