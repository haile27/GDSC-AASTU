def calculate_word_lengths(words):
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))
    return word_lengths

# Example 
words = ["apple", "banana", "orange", "grape"]
lengths = calculate_word_lengths(words)
print(lengths)