"""
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL

示例 2:
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL

说明:
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         head1 = ListNode(None)
#         head2 = ListNode(None)
#         cur1 = head1
#         cur2 = head2
#         flag = True
#
#         while head is not None:
#             if flag:
#                 cur1.next = head
#                 cur1 = cur1.next
#
#             else:
#                 cur2.next = head
#                 cur2 = cur2.next
#             head = head.next
#             flag = not flag
#         cur1.next = head2.next
#         cur2.next = None
#         return head1.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        even = head
        odd = head.next
        tmp = odd

        while even.next is not None and odd.next is not None:
            even.next = even.next.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next
        even.next = tmp
        return head






