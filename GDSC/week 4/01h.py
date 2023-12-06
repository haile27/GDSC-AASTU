#a
'''
def greet(name):
    print(f"hello, {name}! how are u.")
greet("hailu")

#b
def add_numbers(num1, num2):
    return num1 + num2
add_numbers(1, 2)    

#c
def print_args(*args):
    for i in args:
        print(i)
print_args(1, 3, 2, 5, 7, 9)

#d
def calculate_average(*args):
    return sum(args) / len(args)
ave = calculate_average(1, 3, 2, 5, 7, 9)
print(ave)


#ex1
x = lambda a, b : a * b
print(x(5, 6))

#ex2
x = lambda a:a**2
print(x(6))


#3

x = lambda a: "even" if a % 2 == 0 else "odd"
print(x(6))

#filter func

nums = [5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums) 


#map func
nums = [8, 9, 3, 4, 5, 0, 7, 10]
doubled_nums = list(map(lambda x: x*2, nums))
print(doubled_nums)    

#2
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    print("Sum:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
'''
#3
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    res = num1 / num2
    print("Res:", res)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

    
