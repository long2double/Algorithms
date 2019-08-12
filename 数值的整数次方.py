"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        # return base ** exponent
        flip = exponent
        if exponent == 0:
            return 1
        if exponent <= 0:
            exponent = -exponent

        num = 1
        while exponent != 0:
            if exponent & 1 == 1:
                num *= base
            base *= base
            exponent >>= 1

        if flip < 0:
            return 1 / num
        else:
            return num