def display_word_length_distribution(length_frequency):
    sorted_lengths = sorted(length_frequency.keys())

    for length in sorted_lengths:
        frequency = length_frequency[length]
        print(f"Length: {length}, Frequency: {frequency}")