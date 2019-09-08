"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []

        res = []
        self.generate('', n, n, res)
        return res

    def generate(self, item, left, right, res):
        if left == 0 and right == 0:
            res.append(item)
            return

        if left > 0:
            self.generate(item + '(', left - 1, right, res)
        if left < right:
            self.generate(item + ')', left, right - 1, res)
