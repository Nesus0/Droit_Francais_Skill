# REFERENCE — 14 Modes d'Erreur LLM en Recherche Juridique

**Version** : 4.1.7 | **Objectif** : Checklist anti-hallucination

---

## Vue d'Ensemble

Les modèles de langage peuvent commettre des erreurs prévisibles en recherche juridique. Cette référence liste les 14 modes d'erreur les plus fréquents et les contre-mesures correspondantes.

---

## Liste des 14 Modes d'Erreur

### Mode 1 — Numéro d'Article Inventé

**Description** : Le modèle invente un numéro d'article qui n'existe pas.

**Exemple**
> ❌ « L'article L. 9999-1 du Code du travail... »

**Détection**
- Vérifier le format (lettres/nombres plausibles)
- Vérifier sur Légifrance

**Contre-mesure**
```
SI vous ne pouvez pas vérifier l'article :
  MARQUER "[NON VÉRIFIÉ — à confirmer sur Légifrance]"
```

---

### Mode 2 — Cutoff Temporel Ignoré

**Description** : Le modèle忽略 la date limite de ses connaissances.

**Exemple**
> ❌ « L'article L. 1234-1 est toujours en vigueur » (sans mention de modification récente)

**Détection**
- Mentionner la date de référence
- Vérifier les modifications récentes

**Contre-mesure**
```
TOUJOURS indiquer :
"[Réf. : {date} — État : en vigueur/modifié/abrogé]"
"[À vérifier : modifications postérieures à {date}]"
```

---

### Mode 3 — Version du Code Confuse

**Description** : Le modèle utilise une version obsolète du code sans le préciser.

**Exemple**
> ❌ « L'article 1234-1 du Code civil... » (sans préciser la version)

**Détection**
- Les codes sont régulièrement modifiés
- Une même référence peut avoir changé de contenu

**Contre-mesure**
```
PRÉCISER :
"Code civil, art. 1234-1 (version en vigueur au {date})"
```

---

### Mode 4 — Juridiction Confuse

**Description** : Le modèle confond les différentes juridictions.

**Exemple**
> ❌ « Selon la Cour de cassation, en matière administrative... »

**Détection**
- Vérifier la chambre ou la formation
- Distinguer Cass./CE/CC/CJUE/CEDH

**Contre-mesure**
```
TOUJOURS préciser :
"Chambre : {Civ. 1re, Civ. 2e, Com., Soc.}"
"Formation : {CE, CAA, TA, Ass. plén.}"
```

---

### Mode 5 — Analogie Non Vérifiée

**Description** : Le modèle étend une solution jurisprudentielle par analogie non justifiée.

**Exemple**
> ❌ « Par analogie avec la jurisprudence X, on peut appliquer... »

**Détection**
- Vérifier que l'analogie est fondée sur un texte ou une jurisprudence expresse
- Distinguer interpretation et extension

**Contre-mesure**
```
SI analogie :
  MARQUER "[Analogie non vérifiée — à confirmer]"
  PRÉCISER le fondement de l'extension
```

---

### Mode 6 — Décret d'Application Oublié

**Description** : Le modèle cite un article sans vérifier l'existence du décret d'application.

**Exemple**
> ❌ « L'article L. 1234-1 s'applique immédiatement » (sans mention du décret)

**Détection**
- Vérifier si un décret d'application est prévu
- Certains articles ne sont applicables qu'après décret

**Contre-mesure**
```
SI décret prévu :
  MARQUER "[Décret d'application à vérifier]"
```

---

### Mode 7 — Renvois Inter-Textes Ignorés

**Description** : Le modèle cite un article sans vérifier les renvois à d'autres textes.

**Exemple**
> ❌ « L'article X s'applique » (sans vérifier les exceptions des articles Y et Z)

**Détection**
- Vérifier les renvois dans le texte de l'article
- Vérifier les exceptions et conditions

**Contre-mesure**
```
TOUJOURS vérifier :
- Renvois à d'autres articles
- Exceptions expresses
- Conditions de fond
```

---

### Mode 8 — Dispositions Transitoires Oubliées

**Description** : Le modèle ne mentionne pas les dispositions transitoires.

**Exemple**
> ❌ « Cette loi s'applique à compter du {date} » (sans mention des transitoires)

**Détection**
- Vérifier les articles transitoires
- Certaines lois prévoient des délais d'application

**Contre-mesure**
```
SI dispositions transitoires :
  MARQUER "[Application : {date} — Dispositions transitoires : {...}]"
```

---

### Mode 9 — Champ Territorial Non Vérifié

**Description** : Le modèle applique une règle à un territoire où elle n'est pas en vigueur.

**Exemple**
> ❌ « Cette loi s'applique en Nouvelle-Calédonie » (alors qu'elle n'y est pas applicable)

**Détection**
- Vérifier le champ territorial du texte
- Distinguer France métropolitaine, DOM-TOM, Nouvelle-Calédonie

**Contre-mesure**
```
TOUJOURS préciser :
"[Champ territorial : France métropolitaine]"
"[DOM-TOM : vérifier l applicability]"
"[Nouvelle-Calédonie : texte non applicable]"
```

---

### Mode 10 — Logique Cumulative/Alternative Confuse

**Description** : Le modèle présente des conditions comme cumulatives alors qu'elles sont alternatives (ou inversement).

**Exemple**
> ❌ « Les trois conditions doivent être remplies » (alors qu'une seule suffit)

**Détection**
- Vérifier le connecteur logique dans le texte (« et » vs « ou »)
- Distinguer conditions nécessaires et suffisantes

**Contre-mesure**
```
PRÉCISER :
"Conditions cumulatives : {...}"
"Conditions alternatives : {...}"
```

---

### Mode 11 — Faux Positif Textuel

**Description** : Le modèle cite un texte avec une formulation légèrement différente de l'original.

**Exemple**
> ❌ « L'article dispose que "nul ne peut être licencié" » (alors que le texte dit « sans motif réel et sérieux »)

**Détection**
- Vérifier la citation exacte
- Ne jamais présumer de la formulation

**Contre-mesure**
```
SI citation :
  VÉRIFIER le texte exact
  MARQUER "[Citation approximative — vérifier]"
```

---

### Mode 12 — Citation Doctrinale Comme Norme

**Description** : Le modèle présente une opinion doctrinale comme une règle de droit.

**Exemple**
> ❌ « Selon X, l'article doit être interprété ainsi... » (sans préciser que c'est une opinion)

**Détection**
- Distinguer source normative (loi, jurisprudence) de doctrine
- La doctrine n'a pas de force obligatoire

**Contre-mesure**
```
TOUJOURS distinguer :
"[Droit positif] : « L'article X dispose... »"
"[Doctrine — X, Dalloz 2023] : « Selon X... »"
```

---

### Mode 13 — Prescription et Forclusion Confondues

**Description** : Le modèle confond prescription (extinctive de droit) et forclusion (péremption).

**Exemple**
> ❌ « La forclusion est de 5 ans » (alors qu'il s'agit de prescription)

**Détection**
- Vérifier la nature du délai (prescription vs forclusion)
- Distinguer les effets (extinction du droit vs perte de la voie de droit)

**Contre-mesure**
```
TOUJOURS préciser :
"Prescription : {délai} — extinction du droit"
"Forclusion : {délai} — perte de la voie de recours"
```

---

### Mode 14 — Qualification Automatique

**Description** : Le modèle qualifie automatiquement un fait sans vérifier les conditions.

**Exemple**
> ❌ « C'est un contrat de travail » (sans vérifier les critères de subordination)

**Détection**
- Poser la question de qualification
- Vérifier les critères de la qualification

**Contre-mesure**
```
SI qualification juridique :
  MARQUER "[À qualifier — vérifier les critères]"
  LISTER les critères de qualification
```

---

## Checklist Rapide

Avant chaque réponse juridique, vérifiez :

```
□ Référence vérifiable sur Légifrance ?
□ Date de référence mentionnée ?
□ Version du code précisée ?
□ Juridiction correctement identifiée ?
□ Analogie fondée sur un texte ?
□ Décret d'application vérifié ?
□ Renvois inter-textes vérifiés ?
□ Dispositions transitoires mentionnées ?
□ Champ territorial précisé ?
□ Connecteurs logiques corrects ?
□ Citation textuelle exacte ?
□ Doctrine distinguée du droit positif ?
□ Prescription/forclusion distinguées ?
□ Qualification vérifiable ?
```

---

## Règle d'Or

> **Quand vous avez un doute sur une référence, marquez-la `[NON VÉRIFIÉ]` au lieu de l'inventer.**

---

*Cette référence fait partie du skill Droit Francais Skill v4.1.7*
