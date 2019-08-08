"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers == []:
            return ''
        length = len(numbers)
        for i in range(length - 1):
            for j in range(length - 1 - i):
                if str(numbers[j]) + str(numbers[j + 1]) > str(numbers[j + 1]) + str(numbers[i]):
                    numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]
        return int(''.join(map(str, numbers)))