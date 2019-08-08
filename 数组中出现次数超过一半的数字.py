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