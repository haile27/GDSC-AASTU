def find_shortest_word(text):
    words = text.split()
    shortest_word = None
    shortest_length = float('inf')

    for word in words:
        if len(word) < shortest_length:
            shortest_word = word
            shortest_length = len(word)

    return shortest_word, shortest_length