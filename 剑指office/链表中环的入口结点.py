"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None

        head = ListNode(0)
        head.next = pHead

        fast = head
        low = head
        meetNode = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            low = low.next
            if fast == low:
                meetNode = low
                break

        if meetNode is None:
            return None

        cur = head
        while meetNode != cur:
            meetNode = meetNode.next
            cur = cur.next
        return cur


