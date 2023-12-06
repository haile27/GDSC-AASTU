total_sum = 0
count_three_or_five = 0

for i in range(1, 51):
    if i % 2 == 0:
        total_sum += i
        if i % 3 == 0:
            print("Three")
            count_three_or_five += 1
        elif i % 5 == 0:
            print("Five")
            count_three_or_five += 1
        else:
            print(i)

print("Total sum:", total_sum)
print("Count of numbers replaced with 'Three' or 'Five':", count_three_or_five)
