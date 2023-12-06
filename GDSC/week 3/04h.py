def numList(list):
    n = len(list)
    sum = 0
    for i in range(0, n-1):
        if i > 0:
            sum += i  
    return sum
list = [2, -4, 6, -6, 8]
result = numList(list)
print(result)    



