def display_word_frequencies(text):
    words = text.split()
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    sorted_frequency = sorted(word_frequency.items(), key=lambda x: (-x[1], x[0]))
    for word, frequency in sorted_frequency:
        print(f"Word: {word}, Frequency: {frequency}")

#Example
text = "This is a sample text. It is just an example."
display_word_frequencies(text)        