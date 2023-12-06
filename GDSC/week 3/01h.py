def oddEven():
    num = int(input("Enter a num: "))
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
x = oddEven()
print(x)