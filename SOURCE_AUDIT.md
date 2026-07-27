# Audit des sources

Date de consultation des pages et sondes : 2026-07-27 (Europe/Paris). Une
sonde HTTP réussie établit seulement l'accessibilité de l'URL au moment du test;
elle ne prouve ni la consultation d'un document précis, ni sa vigueur.

## Registre actuel

`references/sources.json` contient 17 entrées et décrit des parcours de
recherche. Il ne contient pas de date de vérification, de version, de hash, de
preuve d'ouverture, de licence détaillée, de quota ou de résultat de contrôle.
Le validateur vérifie la forme, les identifiants et les champs requis
(`tools/validate_sources.py:11-114`), pas la réalité juridique des métadonnées.

| ID | Organisme / titre de la page d'accueil | Nature et portée déclarées | Sonde 2026-07-27 | Limite à conserver |
| --- | --- | --- | --- | --- |
| `legifrance` | DILA, « Legifrance » | Texte et publication officiels; portée selon texte et date | 403 depuis la sonde | Accès à retenter; vérifier le document et la vigueur |
| `jorf` | DILA, « Journal officiel » | Publication officielle | 403 depuis la sonde | Publication et entrée en vigueur à distinguer |
| `kali` | DILA, « Conventions collectives » | Accords collectifs | 403 depuis la sonde | IDCC, extension et champ à vérifier |
| `judilibre` | Cour de cassation, « Recherche Judilibre » | Jurisprudence judiciaire publiée | accessible/redirigée | Ne couvre pas automatiquement toutes les juridictions |
| `justice-administrative` | Conseil d'État, « ArianeWeb » | Jurisprudence administrative disponible | accessible/redirigée | Publication sélective et métadonnées à contrôler |
| `conseil-constitutionnel` | Conseil constitutionnel, site officiel | Décisions et publications constitutionnelles | accessible/redirigée | Portée propre aux décisions constitutionnelles |
| `eurlex` | Union européenne, « EUR-Lex » | Textes officiels de l'UE | accessible/redirigée | Applicabilité et transposition à vérifier |
| `curia` | CJUE, « CURIA » | Jurisprudence de l'UE | 503 depuis la sonde | Refaire la vérification; ECLI/affaire requis |
| `hudoc` | CEDH, « HUDOC » | Jurisprudence CEDH | accessible/redirigée | Statut de l'arrêt et portée à vérifier |
| `boss` | Ministère chargé du budget, « BOSS » | Doctrine administrative sociale | connexion réinitialisée | Doctrine administrative, non texte général |
| `bofip` | DGFiP, « BOFiP » | Doctrine fiscale administrative | accessible/redirigée | Portée selon document et conditions légales |
| `cnil` | CNIL, site officiel | Décisions et recommandations | accessible/redirigée | Distinguer décision, recommandation et guide |
| `amf` | AMF, site officiel | Décisions et doctrine de marché | accessible/redirigée | Portée selon type de document |
| `acpr` | ACPR/Banque de France, site officiel | Décisions et doctrine bancaire/assurance | accessible/redirigée | Vérifier l'instrument et son destinataire |
| `autorite-concurrence` | Autorité de la concurrence, site officiel | Décisions et lignes directrices | accessible/redirigée | Ne pas généraliser une décision individuelle |
| `inpi` | INPI, service public | Registres et information administrative | accessible/redirigée | Une fiche de registre n'est pas une règle normative |
| `daj-commande-publique` | DAJ, économie.gouv.fr | Doctrine et guides de commande publique | 403 depuis la sonde | Guide non substitutif au texte contraignant |

## Écarts et actions

- `HIGH-SRC-001` — Le registre peut être interprété comme un état de fraîcheur
  alors qu'il n'est qu'un routage. Correction documentaire réalisée dans les
  rapports; la preuve par source doit rester externe et datée.
- `HIGH-SRC-002` — Les 403/503 et la réinitialisation de connexion imposent le
  statut `[NON VERIFIE]` pour toute citation non ouverte dans la session.
- `MEDIUM-SRC-003` — Les champs `authority_level`, `nature_normative` et
  `opposability` sont des catégories internes; ils ne remplacent pas l'analyse
  du document précis.

## Format recommandé pour une preuve future

Pour chaque consultation, conserver hors du registre ou dans un rapport daté :
`source_id`, URL finale, titre, organisme, date/heure Europe-Paris, type de
document, identifiant, version ou date de mise à jour, passage contrôlé, statut
de vigueur, licence/CGU, résultat HTTP et limites. Ne pas archiver de données
personnelles inutiles.

## Verdict sources

Les sources officielles listées sont plausibles comme points d'accès, mais leur
présence n'est pas une preuve de consultation. Aucune nouvelle source n'est
ajoutée au registre dans cet audit, car l'autorité, la licence et le format de
réutilisation doivent être confirmés au niveau du service ou document précis.
