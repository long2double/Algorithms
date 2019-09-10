"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：
结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树

例如：
给定 BST [1,null,2,2],
   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序
进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_count = -2 ** 32
        self.max_num = -2 ** 32
        self.last = None
        self.count = 1
        self.last_ = None
        self.res = []

    def findMode(self, root: TreeNode) -> List[int]:
        self.find(root)
        return self.printTree(root, self.max_count)

    def find(self, root):
        if root is None:
            return

        self.find(root.left)
        if self.last is None:
            self.last = root.val
            self.max_count = 1
            self.max_num = root.val
        else:
            if self.last == root.val:
                self.count += 1
                if self.count > self.max_count:
                    self.max_count = self.count
                    self.max_num = root.val
            else:
                self.count = 1
                self.last = root.val
        self.find(root.right)

    def printTree(self, root, max_count):
        if root is None:
            return

        self.printTree(root.left, max_count)
        if self.last_ is None:
            self.last_ = root.val
            self.count = 1
            if self.count == max_count:
                self.res.append(root.val)
        else:
            if self.last_ == root.val:
                self.count += 1
                if self.count == max_count:
                    self.res.append(root.val)
            else:
                self.count = 1
                if self.count == max_count:
                    self.res.append(root.val)
                self.last_ = root.val
        self.printTree(root.right, max_count)
        return self.res