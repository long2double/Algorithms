"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            j = 1
            dp[i] = i
            while i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


if __name__ == '__main__':
    S = Solution()
    s = 4696
    print(S.numSquares(s))
