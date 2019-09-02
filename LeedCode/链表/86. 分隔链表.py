"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = ListNode(None)
        head2 = ListNode(None)

        cur1 = head1
        cur2 = head2
        while head is not None:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
                head = head.next
            else:
                cur2.next = head
                cur2 = cur2.next
                head = head.next
        cur1.next = head2.next
        cur2.next = None
        return head1.next
