# Liber Primus Decoder

Outil simple en Python pour traduire des textes codés en runes anglo-saxonnes vers l'alphabet latin et calculer la valeur gématrique (gematria) de textes latins.

---

## Fonctionnalités

- **Traduction runes → latin** : conversion d’un texte runique utilisant un alphabet anglo-saxon simplifié en lettres latines.
- **Calcul de la valeur gématrique** : somme des valeurs numériques associées aux lettres A-Z (A=1, B=2, ..., Z=26).

---

## Installation

1. Cloner ou télécharger le fichier `primusdecoder.py` dans un dossier local.
2. Assurez-vous d'avoir Python 3 installé (compatible avec Python 3.6+).
3. Aucune dépendance externe nécessaire.

---

## Utilisation

Lancez le script dans un terminal :

```bash
python primusdecoder.py
```

Vous aurez un menu interactif avec trois options :

1. Traduire runes → latin

Entrez un texte runique (exemple : ᚠᚢᚦᚨᚱ)
Le programme vous affichera la traduction en lettres latines (futhar).

2. Calculer valeur gématrique

Entrez un texte latin (exemple : HELLO)
Le programme vous donnera la somme des valeurs des lettres (H=8 + E=5 + L=12 + L=12 + O=15 = 52).

3. Quitter

Sortie du programme.

---

## Format d'entrée

Runes : Utilisez les caractères runiques anglo-saxons Unicode (ex: ᚠ, ᚢ, ᚦ, etc.).

Latin : Lettres alphabétiques A-Z, insensible à la casse. Les autres caractères sont ignorés dans le calcul gématrique.

---

## Limitations

La table de conversion runes → latin est basique et peut être étendue selon vos besoins.

La valeur gématrique est calculée uniquement sur les lettres A-Z en majuscules.

Le programme ne déchiffre pas les codes complexes ni les substitutions avancées.

---

## Personnalisation

Modifier le dictionnaire RUNE_TO_LATIN dans le fichier pour ajouter ou corriger les correspondances runiques.

Étendre la fonction gématrique si vous souhaitez un autre système de valeurs.

Ajouter des fonctionnalités de décodage plus avancées selon vos besoins.

--- 

## Avertissement

Cet outil est éducatif et destiné à expérimenter avec des textes codés, notamment liés au Liber Primus ou à d’autres textes runiques. 
Il ne prétend pas résoudre automatiquement tous les mystères cryptographiques.
