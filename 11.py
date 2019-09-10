class TNode:
    def __init__(self, x=None):
        self.lchild = None
        self.rchild = None
        self.val = x


def listcreattree(root,llist,i):
    if i<len(llist):
        if llist[i] == -1:
            return None
        else:
            root=TNode(llist[i])
            root.left=listcreattree(root.left,llist,2 * i+1)
            root.right=listcreattree(root.right, llist,2 * i+2)
            return root
    return root


def lowestCommonAncestor(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    return root


if __name__ == '__main__':
    n = int(input())
    # node_list = list(map(int, input().split()))
    # left, right = list(map(int, input().split()))
    node_list = [9, 6, 15, 2, -1, 12, 25, -1, -1, -1, -1, -1, -1, 20, 37]
    root = TNode()
    # left_node = TNode(left[0])
    # right_node = TNode(right[1])
    left_node = TNode(15)
    right_node = TNode(20)
    listcreattree(root, node_list, 0)
    node = lowestCommonAncestor(root, left_node, right_node)
    if node is None:
        print(-1)
    else:
        print(node.val)





