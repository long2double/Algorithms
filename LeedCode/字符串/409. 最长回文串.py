"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:
输入:
"abccccdd"
输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        di = {}
        for i in s:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1

        length = 0
        flag = 0
        for key, value in di.items():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                flag = 1

        return length + flag