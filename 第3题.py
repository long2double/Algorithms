# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        if listNode.next is None:
            return listNode

        head = ListNode(0)
        head.next = listNode

        cur = head.next.next
        head.next.next = None
        head.next.next = None

        while cur.next is not None:
            next = cur.next
            cur.next = head.next
            head.next = cur
            cur = next

        cur.next = head.next
        head.next = cur

        li = []
        while head.next is not None:
            head = head.next
            li.append(head.val)
        return li
