'''#1
def even_odd():
    x = int(input("Enter a num:"))
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

y = even_odd()
print(y)


#2
def maxNum():
    a = int(input("a = "))
    b = int(input("b = "))
    if a > b:
        return "a is maximum number"
    else:
        return "b is maximum number"
result = maxNum() 
print(result)

#3
def longest():
    str = input("Enter a simple text:")
    n = len(str)
    if n > 10:
        return "Longest"
    else:
        return "Short"
text = longest()
print(text)


#4
def listSum(list):
    sum = 0
    for i in range (list):
        sum += i
        return i
user_input = int(input("Enter a list: "))
x_list = listSum(user_input)
print(sum)    
'''
#6
n = int(input("Enter a num:"))
def loop(n):
    for i in range(1, n):
        return i
range = loop(n)  
print(range)  









