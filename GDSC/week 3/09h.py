def reverse_strings(strings):
    for string in strings:
        reversed_string = string[::-1]
        print(reversed_string)

string_list = ["hello", "world", "python"]
reverse_strings(string_list)
