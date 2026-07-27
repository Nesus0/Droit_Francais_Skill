# Journal des modifications

## [4.1.6] - 2026-07-27

### Préparation open source

- Ajout de modèles d'issues, de pull request et de gouvernance minimale.
- Mise à jour de la documentation de contribution, sécurité, maturité et surface publique.
- Migration des actions CI vers les versions officielles Node 24 épinglées par SHA.
- Restriction de l'archive de release aux seuls fichiers suivis par Git afin
  d'exclure les sorties locales de campagnes LLM et tout fichier non versionné.
- Le contrôle public de CI vérifie désormais aussi les métadonnées Git de
  l'historique après assainissement.
- Reconstruction de l'historique public à partir de l'arbre audité afin de
  retirer les métadonnées personnelles des commits, tags et anciennes refs.

## [4.1.5] - 2026-07-27

### Audit

- Ajout des rapports d'audit des sources, de la couverture jurisprudentielle,
  du comportement, de la préparation de release et du modèle de menace.
- Extension des cas déclaratifs aux sources inaccessibles, à la temporalité,
  aux injections de prompt, à la hiérarchie des sources et à la vie privée.
- Clarification qu'aucune évaluation multi-modèle n'est exécutée par le dépôt.
- Ajout des audits des affirmations publiques, citations, fraîcheur, adaptateurs,
  reproductibilité et confidentialité.
- Extension du corpus adversarial à 28 cas et ajout de tests déclaratifs de
  références plausibles inexistantes, textes abrogés, versions concurrentes,
  juridictions erronées et injections documentaires.
- Générateur ZIP déterministe avec comparaison automatique de deux SHA-256.
- Actions GitHub épinglées par SHA complet, matrice adaptateurs exécutable et
  runner LLM opt-in avec sorties locales ignorées par Git.

## [4.1.4] - 2026-07-26

### Corrige

- Alignement du changelog avec la version de release publiee.

## [4.1.3] - 2026-07-26

### Corrige

- Nom d'artefact Quality rendu deterministe par commit.

## [4.1.2] - 2026-07-26

### Corrige

- Exclusion des caches Python et fichiers `.pyc` des archives de distribution.

## [4.1.1] - 2026-07-26

### Corrige

- Detection GitHub de la licence CC BY-SA 4.0 via le texte canonique SPDX.
- Liens ArianeWeb et HUDOC invalides dans le registre documentaire.
- Publication des releases generalisee a tous les tags versionnes `v*`.

## [4.1.0] - 2026-07-25

### Ajoute

- Noyau portable independant des fournisseurs.
- Profils operationnels pour avocat, contentieux, entreprise, RH et CSE.
- Registre des sources publiques officielles et validateurs sans dependance.
- Evaluations comportementales multi-modele.
- Correspondances documentees pour ChatGPT, Claude, Gemini, Perplexity et les
  produits generiques.

### Securite

- Garanties explicites contre l'invention de sources et la falsification de
  preuves.
- Protocole d'acces degrade lorsque les sources ne sont pas accessibles.
