def average_word_length(text):
    words = text.split()
    t_length = 0

    for word in words:
        t_length += len(word)
    return t_length / len(words)

#example
text = ("My name is hailu gashaw")
averageLength = average_word_length(text)
print("average length:", averageLength)
