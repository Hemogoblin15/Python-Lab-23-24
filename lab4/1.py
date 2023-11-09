class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print(stack.peek()) 

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

