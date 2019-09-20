class TNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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
        root = TNode(data_li[0])

        for i in range(1, len(data_li)):
            self.binary_insert(root, TNode(data_li[i]))

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



    def build_tree(self, array, l, r):
        if l > r:
            return
        mid = (l + r) // 2
        root = TNode(array[mid])
        root.left = self.build_tree(array, l, mid - 1)
        root.right = self.build_tree(array, mid + 1, r)
        return root

    def print_tree(self, root):
        if root is None:
            return
        print(root.val, end=' ')
        self.print_tree(root.left)

        self.print_tree(root.right)


if __name__ == '__main__':
    S = Solution()
    num = [1,2,3,4,5,6]
    root = S.build_tree(num, 0, len(num) - 1)
    print('前序:')
    S.print_tree(root)
    data = S.serialize(root)
    print('\n序列化:', data)
    root = S.deserialize(data)
    print('\n反序列化:')
    S.print_tree(root)
