"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8

解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

注意:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""


class Solution:
    def maxProfit(self, prices, fee):
        max_without = 0
        max_with = -prices[0]
        for i in range(1, len(prices)):
            max_without = max(max_without, prices[i] + max_with - fee)  # 当天卖不卖的最高利润
            max_with = max(max_with, max_without - prices[i])  # 当天买不买的最高利润
        return max_without


# prices = list(map(int, input().split()))
# length = len(prices)
# if length < 2:
#     print(0)
# dp1 = [0] * length
# dp2 = [0] * length
# min_val = prices[0]
# max_val = prices[-1]
#
# for i in range(1, length):
#     dp1[i] = max(dp1[i - 1], prices[i] - min_val)
#     min_val = min(min_val, prices[i])
#
# for i in range(length - 2, -1, -1):
#     dp2[i] = max(dp2[i + 1], max_val - prices[i])
#     max_val = max(max_val, prices[i])
#
# dp = [dp1[i] + dp2[i] for i in range(length)]
# print(max(dp))

