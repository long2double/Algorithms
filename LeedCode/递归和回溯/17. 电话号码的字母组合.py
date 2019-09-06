"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution:
    def letterCombinations(self, digits: str):
        # 迭代
        if digits is None or digits == '':
            return []

        has_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = ['']
        for num in digits:
            result = []
            for s in res:
                for string in has_map[num]:
                    result.append(s + string)
            res = result
        return res


class Solution:
    def __init__(self):
        self.res = []
        self.has_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str):
        if digits is None or digits == '':
            return []

        self.findLetter(digits, 0, '')
        return self.res

    def findLetter(self, digits, index, s):
        if index == len(digits):
            self.res.append(s)
            return

        num = digits[index]
        letter = self.has_map[num]
        for i in letter:
            self.findLetter(digits, index + 1, s + i)
        return



