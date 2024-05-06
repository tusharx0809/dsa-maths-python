def add_binary(num1,num2):
    int1 = int(num1,2)
    int2 = int(num2,2)
    sum_nums = int1 + int2
    return bin(sum_nums)[2:]

print(add_binary('11','1'))