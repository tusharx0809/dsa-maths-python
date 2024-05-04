# Sum of digits of a given number
def sum_of_digits(num):
    if num < 10 and num > -10:
        return num
    sum_of_digits = 0
    while num != 0:
        dig = num % 10
        sum_of_digits += dig
        num = num // 10
    return sum_of_digits
num = 123
print("The sum of digits", num ,"is: ", sum_of_digits(num)) # The sum of digits 123 is:  6



#Sum of digits using python inbuilt functionality
def sum_Of_digits(num):
    sum_Of_digits = sum(int(i) for i in str(num))
    return sum_Of_digits
num2 = 456
print("The sum of digits", num2 ,"is: ", sum_of_digits(num2)) # The sum of digits 456 is:  15

    