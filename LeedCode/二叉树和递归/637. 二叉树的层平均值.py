"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:
输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].

注意：
节点值的范围在32位有符号整数范围内。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return

        queue = []
        queue.append(root)
        res = []
        while queue:
            length = len(queue)
            tmp = []
            for i in range(length):
                cur_node = queue.pop(0)
                tmp.append(cur_node.val)
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
            res.append(sum(tmp) / length)
        return res