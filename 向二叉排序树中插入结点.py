class TNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def BST_insert(self, root, insert):
        if insert.val < root.val:
            if root.left is not None:
                self.BST_insert(root.left, insert)
            else:
                root.left = insert
        else:
            if root.right is not None:
                self.BST_insert(root.right, insert)
            else:
                root.right = insert
        return root


def build_binary_tree(array, l, r):
    if l > r:
        return
    mid = (l + r) // 2
    node = TNode(array[mid])
    node.left = build_binary_tree(array, l, mid - 1)
    node.right = build_binary_tree(array, mid + 1, r)
    return node


def print_tree(root):
    if root is None:
        return

    print_tree(root.left)
    print(root.val, end=' ')
    print_tree(root.right)


if __name__ == '__main__':
    nums = [1, 4, 7, 10, 23, 34, 54, 98, 100]
    root = build_binary_tree(nums, 0, len(nums) - 1)
    print('插入前:')
    print_tree(root)

    print('\n插入后:')
    S = Solution()
    root = S.BST_insert(root, TNode(35))
    print_tree(root)