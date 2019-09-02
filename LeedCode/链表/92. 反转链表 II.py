"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None:
            return head
        if m == n:
            return head

        _head = ListNode(None)
        _head.next = head
        count = 1
        cur = _head
        while count < m:
            cur = cur.next
            count += 1
        start = cur

        while count <= n:
            cur = cur.next
            count += 1
        end = cur

        head_new = ListNode(None)
        head_new.next = start.next
        cur = head_new.next.next
        head_new.next.next = end.next

        while cur != end:
            next = cur.next
            cur.next = head_new.next
            head_new.next = cur
            cur = next
        cur.next = head_new.next
        start.next = cur
        return _head.next
