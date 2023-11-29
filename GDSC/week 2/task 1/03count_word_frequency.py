def count_word_frequency(text):
    word_frequency = {}
    words = text.split()

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

#Example
text = "This is a sample text. It is just an example."
result = count_word_frequency(text)
print(result)