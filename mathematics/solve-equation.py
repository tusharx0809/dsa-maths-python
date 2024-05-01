"""Solving an equation following the rules of BODMAS using stack and postfix notations. Below code converts an infix notation to postfix and solve it"""

def infix_to_postfix(equation):
  operators = ['+','-','*','/','(',')','^']
  prioritiy = { #set the priorities following BODMAS rules
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
  }

  stack = []
  postfix_notation = ''

  for char in equation:
    if char not in operators:
      postfix_notation += char
    elif char == '(':
      stack.append(char)
    elif char == ')':
      while stack and stack[-1] != '(':
        postfix_notation += stack.pop()
      stack.pop()
    else:
      while stack and stack[-1] != '(' and prioritiy[char] <= prioritiy[stack[-1]]:
        postfix_notation += stack.pop()
      stack.append(char)

  while stack:
    postfix_notation += stack.pop()
  return postfix_notation

def evaluate_postfix(equation): 
  stack = []
  equation = equation.replace(' ','') #to handle spaces in postfix notation input
  tokens = list(equation)
  for token in tokens:
    if token in ['+','-','*','/','^']:
      num_first = stack.pop()
      num_second = stack.pop()
      if token == '+':
        stack.append(int(num_second) + int(num_first))
      elif token == '-':
        stack.append(int(num_second) - int(num_first))
      elif token == '*':
        stack.append(int(num_second) * int(num_first))
      elif token == '/':
        stack.append(int(num_second) / int(num_first))
      else:
        stack.append(int(num_second) ** int(num_first))
    else:
      stack.append(token)
  return stack[0]

postfix = infix_to_postfix('(3+4)*(5-2)/7^2')
print(postfix)
print("Solution below:")

print(evaluate_postfix(postfix))


