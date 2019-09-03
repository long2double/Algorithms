"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return root

        stack1 = []
        stack2 = []

        stack1.append(root)
        res = []
        flag = True
        while stack1 or stack2:
            tmp = []
            if flag:
                length = len(stack1)
                for i in range(length):
                    cur_node = stack1.pop()
                    tmp.append(cur_node.val)
                    if cur_node.left is not None:
                        stack2.append(cur_node.left)
                    if cur_node.right is not None:
                        stack2.append(cur_node.right)
            else:
                length = len(stack2)
                for i in range(length):
                    cur_node = stack2.pop()
                    tmp.append(cur_node.val)
                    if cur_node.right is not None:
                        stack1.append(cur_node.right)
                    if cur_node.left is not None:
                        stack1.append(cur_node.left)
            flag = not flag
            res.append(tmp[:])
        return res
    