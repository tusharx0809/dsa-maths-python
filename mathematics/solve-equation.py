def infix_to_postfix(equation):
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
    }
    stack = []
    postfix_notation = ''
    
    for char in equation:
        if char.isdigit():  # Handle multi-digit numbers and decimals
            postfix_notation += char
        elif char == ' ':
            continue
        else:
            postfix_notation += ' '
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix_notation += stack.pop() + ' '
                stack.pop()
            else:
                while stack and stack[-1] != '(' and priority[char] <= priority[stack[-1]]:
                    postfix_notation += stack.pop() + ' '
                stack.append(char)
    
    while stack:
        postfix_notation += ' ' + stack.pop()
    return postfix_notation

def evaluate_postfix(equation):
    stack = []
    tokens = equation.split()
    for token in tokens:
        if token in ['+','-','*','/','^']:
            num_first = float(stack.pop())
            num_second = float(stack.pop())
            if token == '+':
                stack.append(num_second + num_first)
            elif token == '-':
                stack.append(num_second - num_first)
            elif token == '*':
                stack.append(num_second * num_first)
            elif token == '/':
                stack.append(num_second / num_first)
            elif token == '^':
                stack.append(num_second ** num_first)
        else:
            stack.append(float(token))  # Ensure the numbers are pushed as floats
    return stack.pop()

# Testing with a complex expression
postfix = infix_to_postfix('(3+4)*(5-2)/7^2')
print("Postfix:", postfix)
print("Solution:", evaluate_postfix(postfix))
