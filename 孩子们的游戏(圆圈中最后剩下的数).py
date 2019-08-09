"""
题目描述
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个
游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首
歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个
小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小
朋友的编号是从0到n-1)
"""
# -*- coding:utf-8 -*-
class LNode:
    def __init__(self, item=None):
        self.val = item
        self.next = None


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0 or m == 0:
            return -1
        head = LNode()
        cur = head
        for i in range(n):
            node = LNode(i)
            cur.next = node
            cur = cur.next
        cur.next = head.next

        # 注意第一次寻找第m个小朋友时，从head结点开始，后边的寻找不从头结点开始，count=1
        cur = head
        count = 0
        while cur.next != cur:
            for i in range(count, m):
                pre = cur
                cur = cur.next
            if pre.next == head.next:
                head.next = cur.next
                pre.next = head.next
                cur = cur.next
            else:
                pre.next = cur.next
                cur = cur.next
            count = 1
        return cur.val
