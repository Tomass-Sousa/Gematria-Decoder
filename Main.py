# -*- coding: utf-8 -*-

# Table runes simples vers lettres latines (exemple)
RUNE_TO_LATIN = {
    'ᚠ': 'f', 'ᚢ': 'u', 'ᚦ': 'th', 'ᚨ': 'a', 'ᚱ': 'r',
    'ᚲ': 'k', 'ᚷ': 'g', 'ᚹ': 'w', 'ᚺ': 'h', 'ᚾ': 'n',
    'ᛁ': 'i', 'ᛃ': 'j', 'ᛇ': 'eo', 'ᛈ': 'p', 'ᛉ': 'z',
    'ᛋ': 's', 'ᛏ': 't', 'ᛒ': 'b', 'ᛖ': 'e', 'ᛗ': 'm',
    'ᛚ': 'l', 'ᛜ': 'ng', 'ᛞ': 'd', 'ᛟ': 'o'
}

# Table gématrique (valeurs simples A=1, B=2, ..., Z=26)
GEMATRIA_VALUES = {chr(i): i - 64 for i in range(65, 91)}  # A-Z

def runes_to_latin(text):
    """Convertit un texte runique en alphabet latin selon RUNE_TO_LATIN."""
    result = []
    for char in text:
        if char in RUNE_TO_LATIN:
            result.append(RUNE_TO_LATIN[char])
        else:
            result.append(char)  # conserve les autres caractères (espaces, ponctuation)
    return ''.join(result)

def gematria_value(text):
    """Calcule la valeur gématrique d'un texte latin (ignore non A-Z)."""
    text = text.upper()
    total = 0
    for char in text:
        if char in GEMATRIA_VALUES:
            total += GEMATRIA_VALUES[char]
    return total

def main():
    print("=== PrimusDecoder - outil runes & gématria ===\n")

    while True:
        print("Options :")
        print("1) Traduire runes → latin")
        print("2) Calculer valeur gématrique")
        print("3) Quitter")
        choice = input("Choix : ").strip()

        if choice == '1':
            runic_text = input("Texte runique : ").strip()
            latin_text = runes_to_latin(runic_text)
            print(f"→ Traduction : {latin_text}\n")

        elif choice == '2':
            latin_text = input("Texte latin : ").strip()
            value = gematria_value(latin_text)
            print(f"→ Valeur gématrique : {value}\n")

        elif choice == '3':
            print("Bye !")
            break

        else:
            print("Choix invalide, réessayez.\n")

if __name__ == "__main__":
    main()
