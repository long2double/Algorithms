"""
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库
函数。 数值为0或者字符串不是一个合法的数值则返回0。
"""
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0

        for i in s[1:]:
            if i < '0' or i > '9':
                return 0

        if s[0] != '-' and s[0] != '+' and s[0] < '0' and s[0] > '9':
            return 0

        sums = 0
        for index, value in enumerate(s[::-1]):
            if value == '-':
                return -sums
            if value == '+':
                return sums
            sums += (10 ** index) * (ord(value) - 48)
        return sums

