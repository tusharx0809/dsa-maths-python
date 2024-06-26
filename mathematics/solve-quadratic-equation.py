"""Below program is used to calculate the roots of quadratic equation without using RegEx"""

#Quadratic equation can be represented in the form of ax**2+b*x+_c = 0 
#Formula to find the roots of a quadratic equation (-b +- ((math.sqrt(pow(b,2)-4*a*c))))  / (2 * a)
#equation used '2x**2-14*x+24', 'x**2-2*x+2' and '2x**2-9*x+5'
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
    index += 4 # skip x**2
    if equation[index] == '-' or equation[index] == '+':
        b += equation[index]
        index += 1
    while equation[index].isdigit():
        b += equation[index]
        index += 1
    index += 2 # skip *x
    if equation[index] == '-' or equation[index] == '+':
        c += equation[index]
        index += 1
    while index < len(equation) and equation[index].isdigit():
        c += equation[index]
        index += 1

    a = int(a) if len(a) > 0 else 1
    b = int(b) if len(b) > 0 else 1
    c = int(c) if len(c) > 0 else 1

    if pow(b,2)-4*a*c < 0:
        return "No real roots exists for equation!"
    else:
        first_root = (-b + ((math.sqrt(pow(b,2)-4*a*c))))  / (2 * a)
        second_root = (-b - ((math.sqrt(pow(b,2)-4*a*c)))) / (2 * a)
        return first_root, second_root

print(solve_quadratic('2x**2-14*x+24')) # will print two roots of equation as (4.0, 3.0)
print(solve_quadratic('x**2-2*x+2'))# this will print No real roots exists for this equation!
print(solve_quadratic('2x**2-9*x+5'))# will print two roots of equation as (3.850781059358212, 0.6492189406417879)