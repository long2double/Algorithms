"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.

示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pHead1 = ListNode(None)
        pHead1.next = head

        pHead2 = ListNode(None)

        slow = pHead1
        fast = pHead1
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        pHead2.next = slow.next
        slow.next = None

        if pHead2 is not None and pHead2.next is not None:
            cur = pHead2.next.next
            pHead2.next.next = None
            while cur is not None:
                next = cur.next
                cur.next = pHead2.next
                pHead2.next = cur
                cur = next

        cur1 = pHead1.next
        cur2 = pHead2.next
        pHead = ListNode(None)
        pHead_cur = pHead
        flag = True
        while cur1 is not None or cur2 is not None:
            if flag:
                pHead_cur.next = cur1
                pHead_cur = pHead_cur.next
                cur1 = cur1.next
            else:
                pHead_cur.next = cur2
                pHead_cur = pHead_cur.next
                cur2 = cur2.next
            flag = not flag
        # return pHead.next



