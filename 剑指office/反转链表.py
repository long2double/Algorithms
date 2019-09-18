"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead

        head = ListNode(0)
        head.next = pHead

        cur = head.next.next
        head.next.next = None

        while cur.next is not None:
            next = cur.next
            cur.next = head.next
            head.next = cur
            cur = next
        cur.next = head.next
        head.next = cur
        return head.next