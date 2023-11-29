# Write a program that takes a list of numbers as input and prints the sum of all the numbers in the list.
list = [2, 4, 5, 8]
n = len(list)
sum = 0
for i in list:
    sum += i
print(sum)