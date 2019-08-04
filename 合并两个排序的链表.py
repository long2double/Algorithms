# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head = ListNode(0)
        cur = head
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                cur = cur.next
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                cur = cur.next
                pHead2 = pHead2.next

        if pHead1 is not None:
            cur.next = pHead1
        if pHead2 is not None:
            cur.next = pHead2
        return head.next