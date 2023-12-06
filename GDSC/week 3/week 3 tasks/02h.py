# Print the pattern
char = input("Enter a character: ")
for i in range(1, 6):  # 5 lines in the pattern
    if i == 1:  # First line
        print(char * 5)
    elif i == 2:  # Second line
        print((char + ' ') * 5)
    elif i == 3:  # Third line
        print((char * 2 + ' ') * 2)
    elif i == 4:  # Fourth line
        print((char * 3 + ' ') * 2)
    elif i == 5:  # Fifth line
        print(char * 5)