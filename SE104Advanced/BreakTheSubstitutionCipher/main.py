import string

ALPHABET = string.ascii_uppercase
ENGLISH_LETTERS_FREQUENCY_DICT = {
    'A': 8.167,
    'B': 1.492,
    'C': 2.406,
    'D': 4.283,
    'E': 12.702,
    'F': 2.4,
    'G': 1.929,
    'H': 5.987,
    'I': 6.996,
    'J': 0.153,
    'K': 0.772,
    'L': 4.025,
    'M': 2.782,
    'N': 6.749,
    'O': 7.507,
    'P': 1.974,
    'Q': 0.095,
    'R': 6.094,
    'S': 6.327,
    'T': 9.056,
    'U': 2.758,
    'V': 0.978,
    'W': 2.015,
    'X': 0.236,
    'Y': 2.36,
    'Z': 0.074
}

BOOK_FILE_NAME = "encrypted_book.txt"


def get_book_content(file_path):
    with open(file_path, "r") as handle:
        return handle.read()


def get_dict_sorted(dict_to_sort):
    freq_list = []
    inverted_dict = {}
    dict_sorted = []
    for chara, frequency in dict_to_sort.items():
        freq_list.append(frequency)
        frequency = str(frequency)
        inverted_dict[frequency] = chara
    freq_list.sort()
    for frequency in freq_list:
        chara = inverted_dict[str(frequency)]
        dict_sorted.append(chara)
    return dict_sorted


def get_letters_frequency(book):
    letters_frequency = {}
    book = book.upper()
    for letter in ALPHABET:
        letters_frequency[letter] = book.count(letter)
    return letters_frequency


def get_decrypt_key(encrypted_frequency, alphabet_frequency):
    decrypt_key = {}
    for i in range(len(encrypted_frequency)):
        encrypted_chara = encrypted_frequency[i]
        decrypted_chara = alphabet_frequency[i]
        decrypt_key[encrypted_chara] = decrypted_chara
    return decrypt_key


def decrypt_text(text, decrypt_key):
    decrypted_text = ''
    for chara in text:
        if decrypt_key.get(chara.upper()):
            is_lower = chara == chara.lower()
            decrypted_chara = decrypt_key[chara.upper()]
            decrypted_chara = decrypted_chara.lower() if is_lower else decrypted_chara
        else:
            decrypted_chara = chara
        decrypted_text += decrypted_chara
    return decrypted_text


def main():
    encrypted_book = get_book_content(BOOK_FILE_NAME)
    book_letters_dict = get_letters_frequency(encrypted_book)
    letters_frequency = get_dict_sorted(book_letters_dict)
    english_frequency = get_dict_sorted(ENGLISH_LETTERS_FREQUENCY_DICT)
    decrypt_key = get_decrypt_key(letters_frequency, english_frequency)
    decrypted_book = decrypt_text(encrypted_book, decrypt_key)
    print(decrypted_book)


if __name__ == "__main__":
    main()
