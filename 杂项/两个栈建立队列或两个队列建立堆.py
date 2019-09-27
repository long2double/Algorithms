"""
两个栈建立队列或两个队列建立堆
"""


class Stack:
    def __init__(self):
        self.stack = []

    def length(self):
        return len(self.stack)

    def is_empty(self):
        return self.length() == 0

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]


class Solution_Stack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        self.stack1.push(x)

    def pop(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            return
        if self.stack2.is_empty():
            for s in range(self.stack1.length()):
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()


class Queue:
    def __init__(self):
        self.queue = []

    def length(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.length() == 0
    
    def push(self, x):
        self.queue.append(x)
        
    def pop(self):
        if self.is_empty():
            return
        else:
            return self.queue.pop(0)


class Solution_Queue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.flag = True

    def push(self, x):
        if self.queue1.is_empty() and self.queue2.is_empty():
            self.flag = True
        if self.flag:
            self.queue1.push(x)
            self.flag = False
        elif not self.queue1.is_empty():
            self.queue1.push(x)
        elif not self.queue2.is_empty():
            self.queue2.push(x)

    def pop(self):
        if self.queue1.is_empty() and self.queue2.is_empty():
            return
        if not self.queue1.is_empty():
            for i in range(self.queue1.length() - 1):
                self.queue2.push(self.queue1.pop())

            return self.queue1.pop()
        else:
            for i in range(self.queue2.length() - 1):
                self.queue1.push(self.queue2.pop())
            return self.queue2.pop()


if __name__ == '__main__':
    S = Solution_Queue()
    S.push(1)
    print(S.pop())
    S.push(2)
    S.push(3)
    print(S.pop())
    S.push(4)
    S.push(5)
    print(S.pop())
    print(S.pop())
    print(S.pop())


