"""
题目描述
输入两个链表，找出它们的第一个公共结点。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        思路：其实利用栈主要解决就是同时到达第一个结点的问题。那么从链表头出发如何同时到达第一个相同的结点呢? 链表的长度相同就
        可以，其实就是走的结点数目相同。所以可以让其中长的链表先走几步，剩余的长度到短链表的长度相同。
        """
        # write code here
        # if pHead1 is None or pHead2 is None:
        #     return
        #
        # cur1 = pHead1
        # count1 = 1
        # while cur1.next is not None:
        #     cur1 = cur1.next
        #     count1 += 1
        #
        # cur2 = pHead2
        # count2 = 1
        # while cur2.next is not None:
        #     cur2 = cur2.next
        #     count2 += 1
        #
        # if cur2 != cur1:
        #     return
        #
        # if count1 < count2:
        #     n = count2 - count1
        #     cur1 = pHead1
        #     cur2 = pHead2
        #     while cur1 != cur2:
        #         if n > 0:
        #             cur2 = cur2.next
        #             n -= 1
        #         else:
        #             cur2 = cur2.next
        #             cur1 = cur1.next
        # else:
        #     n = count1 - count2
        #     cur1 = pHead1
        #     cur2 = pHead2
        #     while cur1 != cur2:
        #         if n > 0:
        #             cur1 = cur1.next
        #             n -= 1
        #         else:
        #             cur2 = cur2.next
        #             cur1 = cur1.next
        # return cur1
        """
        有个思路，不需要存储链表的额外空间。也不需要提前知道链表的长度。看下面的链表例子：
        0-1-2-3-4-5-null
        a-b-4-5-null
        代码的ifelse语句，对于某个指针p1来说，其实就是让它跑了连接好的的链表，长度就变成一样了。
        如果有公共结点，那么指针一起走到末尾的部分，也就一定会重叠。看看下面指针的路径吧。
        p1： 0-1-2-3-4-5-null(此时遇到ifelse)-a-b-4-5-null
        p2:  a-b-4-5-null(此时遇到ifelse)0-1-2-3-4-5-null
        因此，两个指针所要遍历的链表就长度一样了
        """
        # cur1 = pHead1
        # cur2 = pHead2
        # while cur1 != cur2:
        #     cur1 = cur1.next if cur1 else pHead2
        #     cur2 = cur2.next if cur2 else pHead1
        # return cur1
        """
        思路：两条相交的链表呈Y型。可以从两条链表尾部同时出发，最后一个相同的结点就是链表的第一个相同的结点。可以利用栈来实现。
        时间复杂度有O(m + n), 空间复杂度为O(m + n) 
        """
        stack1, stack2 = [], []
        cur1, cur2 = pHead1, pHead2
        while cur1 is not None:
            stack1.append(cur1)
            cur1 = cur1.next

        while cur2 is not None:
            stack2.append(cur2)
            cur2 = cur2.next

        first = None
        while stack1 and stack2:
            top1 = stack1.pop()
            top2 = stack2.pop()
            if top1 is top2:
                first = top1
            else:
                break
        return first
