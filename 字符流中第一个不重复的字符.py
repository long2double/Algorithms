"""
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.in_stream = []
        self.has_map = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.in_stream:
            if self.has_map[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        self.in_stream.append(char)
        if char not in self.has_map:
            self.has_map[char] = 1
        else:
            self.has_map[char] = 2