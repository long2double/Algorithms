"""
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        """
        思路：
        已知条件：后序序列最后一个值为root；二叉搜索树左子树值都比root小，右子树值都比root大。
        1、确定root；
        2、遍历序列（除去root结点），找到第一个大于root的位置，则该位置左边为左子树，右边为右子树；
        3、遍历右子树，若发现有小于root的值，则直接返回false；
        4、分别判断左子树和右子树是否仍是二叉搜索树（即递归步骤1、2、3）。

        if sequence is None or sequence == []:
            return False

        length = len(sequence)
        for i in range(length):  # 当[1]只有一个元素是length - 1会导致i没有定义
            if sequence[i] > sequence[-1]:
                break

        for j in range(i, length):
            if sequence[j] < sequence[-1]:
                return False

        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
        """

        length = len(sequence)
        if length == 0:
            return False

        while length:
            index = 0
            length -= 1
            while sequence[index] < sequence[length]:
                index += 1
            while sequence[index] > sequence[length]:
                index += 1

            if index < length:  # 找到大于最后元素的位置，然后后边的元素如果有小于的，则返回False
                return False
        return True