def longestString():
    text = input("Enter a string: ")
    n = len(text)
    if n>10:
        return "longest string"
    else:
        return "shortest string"

input = longestString()  
print(input)      