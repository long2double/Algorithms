"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sums = 0
        head = ListNode(None)
        cur = head
        while l1 is not None and l2 is not None:
            yushu = (l1.val + l2.val + sums) % 10
            sums = (l1.val + l2.val + sums) // 10
            cur.next = ListNode(yushu)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            yushu = (l1.val + sums) % 10
            sums = (l1.val + sums) // 10
            cur.next = ListNode(yushu)
            cur = cur.next
            l1 = l1.next

        while l2 is not None:
            yushu = (l2.val + sums) % 10
            sums = (l2.val + sums) // 10
            cur.next = ListNode(yushu)
            cur = cur.next
            l2 = l2.next

        if sums > 0:
            cur.next = ListNode(sums)
            cur = cur.next
        return head.next
