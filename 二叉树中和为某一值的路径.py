# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.path = []
        self.result = []

    def FindPath(self, root, expectNumber):
        # write code here
        if root is not None:
            self.path.append(root.val)
            if root.left is None and root.right is None and sum(self.path) == expectNumber:
                self.result.append(self.path[:])
            else:
                self.FindPath(root.left, expectNumber)
                self.FindPath(root.right, expectNumber)
            self.path.pop()
        return self.result