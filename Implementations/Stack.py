'''
Implementation of a Stack data structure - First in Last out
O(1) push
O(1) pop
O(1) get_size
O(1) peek
'''

class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        self.stack.pop()
    
    def get_size(self):
        return len(self.stack)
    
    def peek(self):
        return self.stack[-1]

if __name__=="__main__":
    stack = Stack()

    print(stack.push(3))
    print(stack.push(2))
    print(stack.push(1))
    print(stack.peek())
    print(stack.pop())
    print(stack.get_size())
