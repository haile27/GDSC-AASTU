def count_word_length_frequency(text):
    words = text.split()
    length_frequency = {}

    for word in words:
        length = len(word)
        if length in length_frequency:
            length_frequency[length] += 1
        else:
            length_frequency[length] = 1

    return length_frequency