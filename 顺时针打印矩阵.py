# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            for i in matrix.pop(0):
                result.append(i)
            matrix = list(zip(*matrix))[::-1]
        return result