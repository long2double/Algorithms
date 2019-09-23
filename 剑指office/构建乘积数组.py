"""
题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。
"""


# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        """
        A = [5,2,3,4]
        left = [1, 5x1, 2x5x1, 3x2x5x1]
        right = [1, 4x1, 3x4x1, 2x3x4x1]
    1 2 3 4 5
           1      2x3x4x5
           1       3x4x5
          2x3       4x5
         1x2x3       5
        1x2x3x4      1
        """
        length = len(A) - 1
        left = [1]
        right = [1]

        for i in range(length):
            left.append(A[i] * left[i])
            right.append(A[-i - 1] * right[i])
        return [left[i] * right[-i - 1] for i in range(len(left))]