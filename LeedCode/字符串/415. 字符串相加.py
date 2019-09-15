"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        tmp1 = 0
        tmp2 = 0
        for index, value in enumerate(num1[::-1]):
            tmp1 += (ord(value) - 48) * 10 ** index

        for index, value in enumerate(num2[::-1]):
            tmp2 += (ord(value) - 48) * 10 ** index
        return str(tmp1 + tmp2)
