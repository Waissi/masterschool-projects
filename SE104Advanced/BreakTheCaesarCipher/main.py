import string
LOWER_DIFF = 32

MESSAGE = """
Jylbujm nby gimn zugiom nblyy qilxm onnylyx ch fcnylunoly, "Yn no, Vlony?" (Ypyh sio, Vlonom?) nbcm yrjlymmcih bum wigy xiqh ch bcmnils ni gyuh nby ofncguny vynlusuf vs ihy'm wfimymn zlcyhx. Nbcm mwyhy, ch qbcwb nby wihmjclunilm ch nby Myhuny ummummchuny Wuymul, cm ihy iz nby gimn xluguncw gigyhnm ih nby Mbueymjyulyuh mnuay. Nby uoxcyhwy bum domn qcnhymmyx nby ulliauhwy uhx bovlcm iz u lofyl qbi bum mioabn, qcnbch u lyjovfcw, ni vywigy u gihulwb, wigjulcha bcgmyfz ni nby aixm. Vlonom, u zlcyhx iz Wuymul uhx syn u guh qbi fipym Ligy (uhx zlyyxig) gily, bum dichyx nby wihmjclunilm ch nby ummummchuncih, u vynlusuf qbcwb cm wujnolyx vs nby nblyy qilxm uvipy ch nbcm zugiom Mbueymjyuly koiny.
"""


def encrypt_char(char, key):
    if char in string.punctuation or char == ' ':
        return char
    diff = LOWER_DIFF if char == char.lower() else 0
    code = ord(char)
    if code + key < 65 + diff:
        return chr((91 + diff) - ((65 + diff) - (code + key)))
    if code + key > 90 + diff:
        return chr((64 + diff) + (code + key - (90 + diff)))
    return chr(code + key)


def encrypt_caesar(text, key):
    encrypted = ''
    for char in text:
        encrypted += encrypt_char(char, key)
    return encrypted


def decrypt_caesar(text, key):
    decrypted = ''
    for char in text:
        decrypted += encrypt_char(char, -key)
    return decrypted


def main():
    number_of_letters_in_alphabet = 26
    for i in range(1, number_of_letters_in_alphabet):
        decrypted = decrypt_caesar(MESSAGE, i)
        correct = input(f"'{decrypted[:30]} ...' Is this one correct? (y or n)")
        if correct == 'y':
            print(decrypted)
            break


if __name__ == "__main__":
    main()
