"""
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        """
        实现思路：
        只需要记录三个指针显示到达哪一步；“|”表示指针,arr表示丑数数组；
        （1）1
        |2
        |3
        |5
        目前指针指向0,0,0，队列头arr[0] * 2 = 2,  arr[0] * 3 = 3,  arr[0] * 5 = 5
        （2）1 2
        2 |4
        |3 6
        |5 10
        目前指针指向1,0,0，队列头arr[1] * 2 = 4,  arr[0] * 3 = 3, arr[0] * 5 = 5
        （3）1 2 3
        2| 4 6
        3 |6 9
        |5 10 15
        目前指针指向1,1,0，队列头arr[1] * 2 = 4,  arr[1] * 3 = 6, arr[0] * 5 = 5
        """
        if index < 7:
            return index

        p2 = p3 = p5 = 0
        res = [1]
        while len(res) < index:
            min_num = min(res[p2] * 2, min(res[p3] * 3, res[p5] * 5))
            if res[p2] * 2 == min_num:
                p2 += 1
            if res[p3] * 3 == min_num:
                p3 += 1
            if res[p5] * 5 == min_num:
                p5 += 1
            res.append(min_num)
        return res[-1]