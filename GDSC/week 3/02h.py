def maxNum():
    a = int(input("a = "))
    b = int(input("b = "))
    if a > b:
        return "a is maximum number"
    elif a < b:
        return "b is maximum number"
    else:
        return "a is equal to b"
        
y = maxNum()
print(y)
    


