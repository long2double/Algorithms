"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        li = list(s)
        for index, key in enumerate(li):
            if key == ' ':
                li[index] = '%20'
        return ''.join(li)


# -*- coding:utf-8 -*-
class Solution:
    # 从后往前进行替换，每个字符只移动一次
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        li = list(s)
        length = len(li)
        space_num = 0
        for i in range(length):
            if li[i] == ' ':
                space_num += 1

        for j in range(space_num * 2):
            li.append(0)

        new_length = len(li)

        n = length - 1  # 17
        m = new_length - 1  # 21
        while n >= 0 and m != n:
            if li[n] != ' ':
                li[m] = li[n]
                m -= 1
            else:
                li[m] = '0'
                m -= 1
                li[m] = '2'
                m -= 1
                li[m] = '%'
                m -= 1
            n -= 1
        return ''.join(li)
