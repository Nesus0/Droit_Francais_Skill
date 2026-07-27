# Adaptateur generique

Cet adaptateur vise les produits qui acceptent un prompt systeme et des
references facultatives.

- utiliser `core/system-prompt.md` comme instructions;
- fournir `core/methodology.md`, le registre, le profil choisi et les domaines;
- configurer outils, navigation, conservation et acces aux fichiers uniquement
  si le produit les prend explicitement en charge.

Si aucun champ d'instructions n'existe, placer le prompt au debut du contexte et
conserver les fichiers joints ou accessibles via le mecanisme documente.
Ne jamais affirmer qu'un fichier ou une source a ete consulte sans preuve de son
accessibilite dans l'interaction en cours.
