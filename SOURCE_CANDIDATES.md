# Sources candidates étudiées

Date des vérifications de pages d'accueil : 2026-07-27 (Europe/Paris). Les
résultats ci-dessous sont des vérifications d'accessibilité et de documentation,
pas des preuves qu'un corpus a été consulté.

| Source | URL officielle | Organisme / catégorie | Contenu et accès | Licence, données et limites | Décision |
| --- | --- | --- | --- | --- | --- |
| API PISTE | https://piste.gouv.fr/ | DILA, API officielle | API Legifrance; compte et credentials nécessaires | Quotas, CGU et droits à confirmer avant intégration; données juridiques potentiellement sensibles selon requête | AJOUTER AVEC RÉSERVES |
| Données DILA | https://www.dila.gouv.fr/ | DILA, données publiques | Jeux et services officiels; ancienne URL data.gouv testée 404 | Vérifier dataset, licence Etalab et version avant chaque import | AJOUTER AVEC RÉSERVES |
| Judilibre | https://www.courdecassation.fr/recherche-judilibre | Cour de cassation, jurisprudence | Recherche et open data selon service | Publication sélective, pseudonymisation et délais; réutilisation à encadrer | DÉJÀ AU REGISTRE |
| Open data justice administrative | https://www.conseil-etat.fr/arianeweb | Conseil d'État, jurisprudence | ArianeWeb et parcours officiels | Couverture et délais variables; la route open-data testée séparément a répondu 404 | AJOUTER AVEC RÉSERVES |
| Service-Public.fr | https://www.service-public.fr/ | DILA, information administrative | Fiches grand public, accès public | Information utile mais non substitutive au texte; mise à jour à contrôler | AJOUTER AVEC RÉSERVES |
| Entreprendre Service-Public | https://entreprendre.service-public.fr/ | DILA, information entreprise | Fiches pratiques et démarches | Source secondaire administrative; ne pas la qualifier de norme | AJOUTER AVEC RÉSERVES |
| Code du travail numérique | https://code.travail.gouv.fr/ | Ministère du Travail, aide pratique | Fiches et simulateurs | Orientation pratique; convention et texte primaire à vérifier | AJOUTER AVEC RÉSERVES |
| Assemblée nationale open data | https://data.assemblee-nationale.fr/ | Assemblée nationale, travaux législatifs | Dossiers, amendements, données ouvertes | Travaux préparatoires non normatifs; licence et schémas à vérifier dataset par dataset | AJOUTER AVEC RÉSERVES |
| Sénat open data | https://www.senat.fr/open-data/ | Sénat, travaux législatifs | Dossiers et données ouvertes | Contexte parlementaire, pas texte en vigueur; versionnement à vérifier | AJOUTER AVEC RÉSERVES |
| BOAMP | https://www.boamp.fr/ | DILA, annonces de marchés | Annonces publiques | Données d'annonce, pas règle générale; API/quotas à confirmer | AJOUTER AVEC RÉSERVES |
| BODACC | https://www.bodacc.fr/ | DILA, annonces civiles et commerciales | Annonces et open data | Données de publication; vérifier réutilisation et correction | AJOUTER AVEC RÉSERVES |
| Défenseur des droits | https://www.defenseurdesdroits.fr/ | Autorité indépendante, décisions/rapports | Publications et recommandations | Doctrine/rapport, portée variable; aucune assimilation à une norme | AJOUTER AVEC RÉSERVES |
| Cour des comptes | https://www.ccomptes.fr/ | Juridictions financières, rapports | Rapports publics | Contrôle et recommandation, pas règle générale; identifier la juridiction | AJOUTER AVEC RÉSERVES |
| HAL | https://hal.science/ | Archive ouverte, doctrine | Articles et dépôts; protection anti-bot observée | Doctrine secondaire, licences hétérogènes, qualité variable | AJOUTER AVEC RÉSERVES |
| theses.fr | https://theses.fr/ | ABES, thèses | Métadonnées et thèses | Doctrine/recherche, pas source normative; droits document par document | AJOUTER AVEC RÉSERVES |
| Persée | https://www.persee.fr/ | Bibliothèque scientifique, doctrine | Articles numérisés | Licences et accès variables; source secondaire | AJOUTER AVEC RÉSERVES |
| OpenEdition | https://www.openedition.org/ | Plateforme scientifique, doctrine | Livres et revues | Licences/accès hétérogènes; aucune valeur normative intrinsèque | AJOUTER AVEC RÉSERVES |

## Candidats rejetés ou à ne pas intégrer directement

- Toute base privée ou payante sans licence de réutilisation et contrat vérifiés.
- Une fiche pratique comme substitut à un texte ou à une décision primaire.
- Une ancienne URL DILA ou une route d'open data renvoyant 404 sans migration
  officielle documentée.
- Un résultat de moteur de recherche sans ouverture du document source.

## Modèle de fiche de source

```yaml
id: exemple-source
nom: Nom officiel
organisme: Organisme responsable
url_officielle: https://...
categorie: normative|jurisprudence|administrative|doctrine
autorite_juridique: portée réelle du document, pas une promesse générale
couverture: juridictions, périodes, formats
date_verification: 2026-07-27
version_ou_identifiant: à renseigner
licence_et_cgu: URL et conditions vérifiées
acces_api_quotas: public, compte ou clé; limites
donnees_personnelles: minimisées/pseudonymisées/inconnues
limites: publication, fraîcheur, territorialité, biais
decision: AJOUTER|AJOUTER AVEC RÉSERVES|NE PAS AJOUTER|À VÉRIFIER
```
