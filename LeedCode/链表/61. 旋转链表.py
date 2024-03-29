"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        pHead = ListNode(None)
        pHead.next = head

        # 求链表的长度
        cur = pHead
        length = 0
        while cur.next is not None:
            cur = cur.next
            length += 1
        k = k % length

        cur = pHead
        count = 1
        while count <= k:
            cur = cur.next
            count += 1

        cur_ = pHead
        while cur.next is not None:
            cur_ = cur_.next
            cur = cur.next
        cur.next = pHead.next
        pHead.next = cur_.next
        cur_.next = None

        return pHead.next
