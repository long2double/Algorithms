"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中
出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 1
        num = numbers[0]
        length = len(numbers)
        for i in range(1, length):
            if num == numbers[i]:
                count += 1
            else:
                count -= 1

            if count == 0:
                num = numbers[i]
                count = 1

        count = 0
        for i in numbers:
            if num == i:
                count += 1
        if count > length // 2:
            return num
        else:
            return 0

        # 哈希
        # di = {}
        # for i in numbers:
        #     if i in di:
        #         di[i] += 1
        #     else:
        #         di[i] = 1
        #
        # length = len(numbers) // 2
        # for key, value in di.items():
        #     if value > length:
        #         return key
        # return 0