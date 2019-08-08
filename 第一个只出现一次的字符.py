"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        di = {}
        for i in s:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1

        for index, value in enumerate(s):
            if di[value] == 1:
                return index
        return -1