"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


# -*- coding:utf-8 -*-
class Stack:
    def __init__(self):
        self.stack = []

    def length(self):
        return len(self.stack)

    def is_empty(self):
        return self.length() == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return
        else:
            return self.stack[-1]


class Solution_Stack:
    def __init__(self):
        self.enqueue = Stack()
        self.dequeue = Stack()

    def push(self, node):
        # write code here
        self.enqueue.push(node)

    def pop(self):
        # return xx
        if self.enqueue.is_empty() and self.dequeue.is_empty():
            return
        if self.dequeue.is_empty():
            while not self.enqueue.is_empty():
                self.dequeue.push(self.enqueue.pop())
        return self.dequeue.pop()



