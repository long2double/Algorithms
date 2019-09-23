"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = exponent
        if exponent < 0:
            exponent = -exponent
        num = 1
        while exponent:
            if exponent & 1 == 1:
                num *= base
            base *= base
            exponent >>= 1
        return num if flag > 0 else 1 / num