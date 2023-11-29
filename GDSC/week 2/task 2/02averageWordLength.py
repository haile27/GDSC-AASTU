def calculate_average_word_length(word_lengths):
    total_length = sum(word_lengths)
    word_count = len(word_lengths)

    if word_count == 0:
        return 0
    average_length = total_length / word_count
    return average_length