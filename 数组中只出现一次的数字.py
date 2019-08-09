"""
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 哈希
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        # has_map = {}
        # for i in array:
        #     if i not in has_map:
        #         has_map[i] = 1
        #     else:
        #         has_map[i] += 1
        #
        # res = []
        # for key, value in has_map.items():
        #     if value == 1:
        #         res.append(key)
        # return res

        # 异或
        """
        思路: 就是使用异或，但是与在成对出现的数字中查找一个单独的数字不同的是需要利用异或结果的最低位为1的flag将数组中的数字分为两类，一类是与flag按位与为0，另一类为不为0，这样再分别异或一次就能够找出这两个数。很是巧妙。其中有一个语法上容易忽略的坑：==的优先级比&高，所以&时需要加括号。
        """
        if array == []:
            return
        tmp = 0
        for i in array:
            tmp ^= i

        idx = 0
        while (tmp & 1) == 0:
            tmp >>= 1
            idx += 1

        a = 0
        b = 0
        for i in array:
            if self.isBit(i, idx):
                a = a ^ i
            else:
                b = b ^ i

        return [a, b]

    def isBit(self, s, idx):
        s >>= idx
        return (s & 1) == 1