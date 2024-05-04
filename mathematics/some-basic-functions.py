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
    return sum(int(i) for i in str(num))
num2 = 456
print("The sum of digits", num2 ,"is: ", sum_of_digits(num2)) # The sum of digits 456 is:  15


# Finding the reverse of a number 
def reverse(num):
    reversed_num = 0
    while num > 0:
        rem = num % 10
        reversed_num = (reversed_num * 10) + rem
        num = num // 10
    return reversed_num
num3 = 123
print("The reverse of", num3, "is:", reverse(num3)) # The reverse of 123 is: 321

# Finding the reverse of number using python inbuilt functionality
def reverse_number(num):
    return int(str(num)[::-1])
num4 = 654
print("The reverse of", num4, "is:", reverse_number(num4))
    
#Find the missing number
#Given an array of length n in which all numbers are present in [0,n] except for one. Find the missing number.
#For example nums = [0,1,2,3,4,5,6,8], here 7 is missing

def missing_number(nums):
    n = len(nums)
    return int((n*(n+1))/2) - sum(nums) #Find the sum of numbers from 0 to n and subtract the sum of nums to get the missing number
nums = [0,1,2,3,4,5,6,8]
print("The missing number is:", missing_number(nums)) # The missing number is: 7