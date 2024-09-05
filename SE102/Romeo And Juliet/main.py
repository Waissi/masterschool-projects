from romeo_and_juliet import PLAY


def top_n_words(freq, n):
    ordered_list = []
    for value in freq.values():
        ordered_list.append(value)
    ordered_list.sort(reverse=True)
    result = {}
    for i in range(n):
        frequency = ordered_list[i]
        for key, value in freq.items():
            if value == frequency:
                if key not in result:
                    result[key] = value
                    if len(result) == n:
                        break
    for key, value in result.items():
        print(f"{key}: {value}")


def words_frequency(words):
    words_dic = {}
    for word in words:
        if word == '' or '[' in word or ']' in word:
            continue
        if word not in words_dic:
            words_dic[word] = 0
        words_dic[word] += 1
    return words_dic


def is_end_of_word(char):
    return char == '.' or char == '!' or char == ',' or char == ';' or char == '?' or char == ' ' or char == '\n' or char == ':'


def get_words(text):
    words = []
    current_word = ''
    for char in PLAY:
        if is_end_of_word(char):
            words.append(current_word)
            current_word = ''
            continue
        current_word += char.lower()
    return words


def main():
    play_words = get_words(PLAY)
    freq = words_frequency(play_words)
    top_n_words(freq, 50)


if __name__ == "__main__":
    main()
