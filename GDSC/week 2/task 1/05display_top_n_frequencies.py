def display_top_n_frequencies(text, n):
    words = text.split()
    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    sorted_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    for i in range(n):
        if i >= len(sorted_frequency):
            break
        word, frequency = sorted_frequency[i]
        print(f"Word: {word}, Frequency: {frequency}")


#Example
text = "This is a text. It is just an example."
N = int(input("Enter the value of N: "))
display_top_n_frequencies(text, N)        