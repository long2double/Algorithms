class Solution:
    def binary_search(self, root, value):
        if root.val == value:
            return value

        if value < root.val:
            if root.left is not None:
                return self.binary_search(root.left, value)
            else:
                return None

        else:
            if root.right is not None:
                return self.binary_search(root.right, value)
            else:
                return None
        