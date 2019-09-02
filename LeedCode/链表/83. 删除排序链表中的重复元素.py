"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        _head = ListNode(None)
        _head.next = head
        cur = _head.next
        while cur is not None and cur.next is not None:
            next = cur.next
            while next.val == cur.val:
                if next.next is not None:
                    next = next.next
                else:
                    next = None
                    break

            cur.next = next
            cur = cur.next
        return _head.next
