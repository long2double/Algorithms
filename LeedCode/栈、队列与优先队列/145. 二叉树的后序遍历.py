"""
给定一个二叉树，返回它的 后序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [3,2,1]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode):
        # 递归
        # if root is None:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        # 迭代
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            cur_node = stack.pop()
            res.append(cur_node.val)
            if cur_node.left is not None:
                stack.append(cur_node.left)
            if cur_node.right is not None:
                stack.append(cur_node.right)
        return res[::-1]

