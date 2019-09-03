"""
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        pHead1 = ListNode(None)
        pHead1.next = head

        slow = pHead1
        fast = pHead1
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        pHead2 = ListNode(None)
        pHead2.next = slow.next
        slow.next = None

        if pHead2.next is None:
            if pHead1.val == pHead2.val:
                return True
            else:
                return False

        cur = pHead2.next.next
        pHead2.next.next = None
        while cur is not None:
            next = cur.next
            cur.next = pHead2.next
            pHead2.next = cur
            cur = next

        while pHead2 is not None:
            if pHead1.val != pHead2.val:
                return False
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return True
