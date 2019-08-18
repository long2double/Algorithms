"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead

        head = ListNode(0)
        head.next = pHead

        cur = head.next
        pre = head
        flag = False
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                cur = cur.next
                flag = True
            else:
                if flag:
                    pre.next = cur.next
                    cur = cur.next
                    flag = False
                else:
                    pre = cur
                    cur = cur.next
        # 判断1，2，3，4，4，5和1，1，1，1
        if flag:
            cur = cur.next
            pre.next = cur
        return head.next