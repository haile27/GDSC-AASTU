def search_word_frequency(text):
    words = text.split()
    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    search_word = input("Enter a word to search: ")

    if search_word in word_frequency:
        frequency = word_frequency[search_word]
        print(f"The word '{search_word}' appears {frequency} time(s) in the text.")
    else:
        print(f"The word '{search_word}' is not found in the text.")

#Example
text = "This is a sample text. It is just an example."
search_word_frequency(text) 