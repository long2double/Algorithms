"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""


class Solution:
    """
    利用当前行加上当前行的下一行对应的最小值，和保存到当前行。自底而上，动态规划
    """
    def minimumTotal(self, triangle):
        length = len(triangle)
        for n in range(length - 2, -1, -1):
            for m in range(len(triangle[n])):
                triangle[n][m] += min(triangle[n + 1][m], triangle[n + 1][m + 1])
        return triangle[0][0]
