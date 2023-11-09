class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.__is_empty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.__is_empty():
            return self.queue[0]
        else:
            return None

    def __is_empty(self):
        return len(self.queue) == 0
    
queue = Queue()

queue.push(5)
queue.push(10)
queue.push(15)

print(queue.peek())

print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
