# Hacker Rank 'Maximum Element' problem

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    
N = int(input())
stk = Stack()
max_elm = []

for i in range(N):
    _input = input().strip()
    
    if ' ' in _input:
        operation, item = _input.split(' ')
        operation, item = [int(operation), int(item)]
    else:
        operation, item = int(_input), 0
    
    if operation == 1:
        stk.push(item)
        if not max_elm or item >= max_elm[-1]:
            max_elm.append(item)
    elif operation == 2:
        if not stk.is_empty():
            value = stk.pop()
            
            if value == max_elm[-1]:
                max_elm.pop()
    elif operation == 3:
        print(max_elm[-1])
             
    
