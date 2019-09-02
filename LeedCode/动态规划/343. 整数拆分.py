"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

说明: 你可以假设 n 不小于 2 且不大于 58。
"""


# 递归
# class Solution:
#     def integerBreak(self, n: int) -> int:
#         return self.breakInteger(n)
#
#     def breakInteger(self, n):
#         self.res = -1
#         if n == 1:
#             return 1
#
#         for i in range(1, n):
#             self.res = max(self.res, max(i * (n - i), i * self.breakInteger(n - i)))
#         return self.res


# 记忆搜索法
# class Solution:
#     def __init__(self):
#         self.res = None
#         self.num = []
#
#     def integerBreak(self, n: int) -> int:
#         self.num = [-1] * (n + 1)
#         return self.breakInteger(n)
#
#     def breakInteger(self, n):
#         self.res = -1
#         if n == 1:
#             return 1
#
#         if self.num[n] != -1:
#             return self.num[n]
#         else:
#             for i in range(1, n):
#                 self.res = max(self.res, max(i * (n - i), i * self.breakInteger(n - i)))
#             self.num[n] = self.res
#         return self.res


# 动态规划
class Solution:
    def integerBreak(self, n):
        dp = [-1] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]


if __name__ == '__main__':
    S = Solution()
    s = 10
    print(S.integerBreak(s))
