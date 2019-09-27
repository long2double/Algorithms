class Node:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.queue = []
        self.root = None

    def createTree(self, array):
        while array:
            if self.root is None:
                self.root = Node(array.pop(0))
                self.queue.append(self.root)
            else:
                cur_node = self.queue[0]
                if cur_node.left is None:
                    cur_node.left = Node(array.pop(0))
                    self.queue.append(cur_node.left)
                else:
                    cur_node.right = Node(array.pop(0))
                    self.queue.append(cur_node.right)
                    self.queue.pop(0)
        return self.root


if __name__ == '__main__':
    def taveral(root):
        if root is None:
            return
        taveral(root.left)
        print(root.val, end=' ')
        taveral(root.right)

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    S = Solution()
    root = S.createTree(array)
    taveral(root)

