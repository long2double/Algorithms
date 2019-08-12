"""
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
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


class Solution:
    def __init__(self):
        self.min_stack = Stack()
        self.data_stack = Stack()

    def push(self, node):
        # write code here
        if self.min_stack.is_empty():
            self.min_stack.push(node)
        elif self.min_stack.peek() >= node:
            self.min_stack.push(node)
        self.data_stack.push(node)

    def pop(self):
        # write code here
        if self.data_stack.peek() == self.min_stack.peek():
            self.min_stack.pop()
        return self.data_stack.pop()

    def top(self):
        # write code here
        return self.data_stack.peek()

    def min(self):
        # write code here
        return self.min_stack.peek()
