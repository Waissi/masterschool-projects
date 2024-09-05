LOWER_DIFF = 32


def is_punctuation(char):
    return char == ' ' or char == '!' or char == '?' or char == ':' or char == '.' or char == ',' or char == ';'


def encrypt_char(char, key):
    if is_punctuation(char):
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
    print(encrypt_caesar('learning', 3) == 'ohduqlqj')
    print(decrypt_caesar('ohduqlqj', 3) == 'learning')
    print(encrypt_caesar('LearniNg', 3) == 'OhduqlQj')
    print(encrypt_caesar('Learning Python is Fun!', 3) == 'Ohduqlqj Sbwkrq lv Ixq!')


if __name__ == "__main__":
    main()
