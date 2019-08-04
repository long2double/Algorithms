# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k == 0:
            return

        fast = head
        count = 1
        while count < k:
            if fast.next is None:
                return
            fast = fast.next
            count += 1

        cur = head
        while fast.next is not None:
            cur = cur.next
            fast = fast.next
        return cur