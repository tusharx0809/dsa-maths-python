def add_binary(num1,num2):
    int1 = int(num1,2)
    int2 = int(num2,2)
    sum_nums = int1 + int2
    return bin(sum_nums)[2:]

print(add_binary('11','1')) #prints 100

def subtract_binary(num1,num2):
    int1 = int(num1,2)
    int2 = int(num2,2)
    subtract_nums = int1 - int2
    return bin(subtract_nums)[2:]

print(subtract_binary('11','1')) #prints 10

def multipy_binary(num1,num2):
    int1 = int(num1,2)
    int2 = int(num2,2)
    product_nums = int1 * int2
    return bin(product_nums)[2:]

print(multipy_binary('11','1')) #prints 11