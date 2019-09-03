"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                res.append(i)
            else:
                if len(res) == 0:
                    return False

                if i == ')' and res[-1] == '(':
                    res.pop()
                elif i == ']' and res[-1] == '[':
                    res.pop()
                elif i == '}' and res[-1] == '{':
                    res.pop()
                else:
                    return False
        return len(res) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        has_map = {'[': ']', '{': '}', '(': ')'}

        res = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                res.append(has_map[i])
            else:
                if len(res) == 0:
                    return False
                if i == ')' and res[-1] == i:
                    res.pop()
                elif i == ']' and res[-1] == i:
                    res.pop()
                elif i == '}' and res[-1] == i:
                    res.pop()
                else:
                    return False
        return len(res) == 0