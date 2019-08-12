"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""


# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        # if n == 0:
            # return 0
        # if n == 1:
            # return 1
        # return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 0
        j = 1
        while n > 1:
            i, j = j, i + j
            n -= 1
        return j