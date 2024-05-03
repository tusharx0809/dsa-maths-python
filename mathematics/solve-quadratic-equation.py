"""Below program is used to calculate the roots of quadratic equation without using RegEx"""

#Quadratic equation can be represented in the form of ax^2+bx+_c = 0 where
#Formula to find the roots of a quadratic equation (-b +- ((math.sqrt(pow(b,2)-4*a*c))))  / (2 * a)
#equation used 
import math
def solve_quadratic(equation):
    equation = equation.replace(' ','')
    a = ''
    b = ''
    c = ''
    index = 0
    while equation[index].isdigit() or equation[index] == '-':
        a += equation[index]
        index += 1
    index += 3 # skip x^2
    if equation[index] == '-' or equation[index] == '+':
        b += equation[index]
        index += 1
    while equation[index].isdigit():
        b += equation[index]
        index += 1
    index += 1 # skip x
    if equation[index] == '-' or equation[index] == '+':
        c += equation[index]
        index += 1
    while index < len(equation) and equation[index].isdigit():
        c += equation[index]
        index += 1

    a = int(a) if len(a) > 0 else 1
    b = int(b) if len(b) > 0 else 1
    c = int(c) if len(c) > 0 else 1

    first_root = (-b + ((math.sqrt(pow(b,2)-4*a*c))))  / (2 * a)
    second_root = (-b - ((math.sqrt(pow(b,2)-4*a*c)))) / (2 * a)
    return first_root, second_root

print(solve_quadratic('2x^2-14x+24')) # will print two roots of equation as (4.0, 3.0)