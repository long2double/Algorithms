"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5

示例 2:
输入: 1->1->1->2->3
输出: 2->3
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
        pre = _head
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
        if flag:
            cur = cur.next
            pre.next = cur
        return _head.next


