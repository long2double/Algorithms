"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证
奇数和奇数，偶数和偶数之间的相对位置不变
"""


# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        # return [i for i in array if i % 2 == 1] + [j for j in array if j % 2 == 0]
        length = len(array)
        jishu = 0
        for i in range(0, length):
            if array[i] % 2 == 1:
                for j in range(i, jishu, -1):
                    array[j], array[j - 1] = array[j - 1], array[j]
                jishu += 1
        return array