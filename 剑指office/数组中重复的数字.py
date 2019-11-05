"""
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几
次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""


# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here

        for j, i in enumerate(numbers):
            c = numbers[:j] + numbers[j + 1:]
            if i in c:
                duplication[0] = i
                return True
        return False


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        has_map = [0] * 10
        for num in numbers:
            if has_map[num] == 0:
                has_map[num] = 1
            else:
                duplication[0] = num
                return True
        return False


# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        length = len(numbers)
        for i in range(length):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                tmp = numbers[i]
                numbers[i], numbers[tmp] = numbers[tmp], numbers[i]
        return False