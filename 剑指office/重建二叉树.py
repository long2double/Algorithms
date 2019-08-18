"""
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历
序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
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
        else:
            return self.dequeue.pop()

