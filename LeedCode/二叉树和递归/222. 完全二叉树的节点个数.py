"""
给出一个完全二叉树，求出该树的节点个数。

说明：
完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:
输入:
    1
   / \
  2   3
 / \  /
4  5 6
输出: 6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    def countNodes(self, root: TreeNode) -> int:
        #         if root is None:
        #             return 0

        #         queue = []
        #         queue.append(root)
        #         count = 0
        #         while queue:
        #             cur_node = queue.pop(0)
        #             count += 1
        #             if cur_node.left is not None:
        #                 queue.append(cur_node.left)
        #             if cur_node.right is not None:
        #                 queue.append(cur_node.right)
        #         return count
        if root is None:
            return 0
        self.countNodes(root.left)
        self.countNodes(root.right)
        self.count += 1
        return self.count
