"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        _head = ListNode(None)
        _head.next = head

        cur = _head.next.next
        _head.next.next = None
        while cur.next is not None:
            next = cur.next
            cur.next = _head.next
            _head.next = cur
            cur = next
        cur.next = _head.next
        _head.next = cur

        return _head.next
