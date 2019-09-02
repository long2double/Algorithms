"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        dp = [[0 for _ in range(m)] for __ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0:  # 第一行为dp的前一行+grid的当前行
                    dp[0][j] = dp[0][j - 1] + grid[0][j]
                elif j == 0:  # 第一列为dp的前一列+grid的当前列
                    dp[i][0] = dp[i - 1][0] + grid[i][0]
                else:  # dp的前一行或前一列的最小值+grid的当前行列
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

