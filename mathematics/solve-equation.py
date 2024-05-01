"""Solving an equation following the rules of BODMAS using stack and postfix notations"""

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

#def evaluate_postfix(equation): 

print(infix_to_postfix('((A+B)*(C-D)/E)^F'))


