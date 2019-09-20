"""
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
设计一个算法来序列化和反序列化二叉搜索树。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
编码的字符串应尽可能紧凑。

注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.data = ''

    def serialize(self, root):
        if root is None:
            return
        self.data += str(root.val) + '#'
        self.serialize(root.left)
        self.serialize(root.right)
        return self.data

    def deserialize(self, data):
        if data is None or data == '':
            return

        data_li = list(map(int, data.strip('#').split('#')))
        root = TreeNode(data_li[0])

        for i in range(1, len(data_li)):
            self.binary_insert(root, TreeNode(data_li[i]))

        return root

    def binary_insert(self, root, insert_node):
        if root is None:
            return

        if insert_node.val < root.val:
            if root.left is not None:
                self.binary_insert(root.left, insert_node)
            else:
                root.left = insert_node
        else:
            if root.right is not None:
                self.binary_insert(root.right, insert_node)
            else:
                root.right = insert_node