"""
1. 把复制的结点链接在原始链表的每一对应结点后面
2. 把复制的结点的random指针指向被复制结点的random指针的下一个结点
3. 拆分成两个链表，奇数位置为原链表，偶数位置为复制链表，注意复制链表的最后一个结点的next指针不能跟原链表指向同一个空结点None，next指针要重新赋值None(判定程序会认定你没有完成复制）
"""
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return

        cur = pHead
        while cur is not None:
            cur_node = RandomListNode(cur.label)
            cur_node.next = cur.next
            cur.next = cur_node
            cur = cur_node.next

        cur = pHead
        while cur is not None:
            cur_node = cur.next
            if cur.random is not None:
                cur_node.random = cur.random.next
            cur = cur_node.next

        cur = pHead
        head = cur.next
        while cur is not None:
            cur_node = cur.next
            cur.next = cur_node.next
            if cur_node.next is None:
                cur_node.next = None
            else:
                cur_node.next = cur_node.next.next
            cur = cur.next
        return head

