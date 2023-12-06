def product_sum(list):
    product = 1
    for i in list:
        product *= i
    return product

list = [2, 3, 7, 8, 9]
x = product_sum(list)  
print(x)      