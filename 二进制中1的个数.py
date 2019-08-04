# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        """
        因为负数是以补码的形式存在的，python负数与0xffffffff按位与
        正好求得该负数的补码状态
        """
        # if n < 0:
        #     n = n & 0xffffffff
        #
        # num = 0
        # while n != 0:
        #     n = n & (n - 1)
        #     num += 1
        # return num
        return bin(n & 0xffffffff).count('1')
