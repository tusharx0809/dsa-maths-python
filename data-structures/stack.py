"""Below is the python program for basic stack - First In Last Out"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def peek(self):
        if len(self.stack) == 0:
            print("Empty Stack!")
        else:
            print(self.stack[-1])
    def pop(self):
        if len(self.stack) == 0:
            print("Empty Stack!")
        else:
            self.stack.pop()

stack = Stack()

stack.peek() #This will print Empty Stack! 
stack.push(1)#first element pushed into stack
stack.push(2)#second element pushed into stack
stack.peek()#this will print the topmost element of stack which is 2
stack.pop()#this will remove the topmost element of stack which is 2
stack.peek()#this will print 1 as 2 was popped in last operation        