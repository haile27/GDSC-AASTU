def find_longest_word(text):
    words = text.split()
    longest_word = ""
    longest_length = 0

    for word in words:
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)

    return longest_word, longest_length