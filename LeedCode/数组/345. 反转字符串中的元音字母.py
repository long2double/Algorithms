"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:
输入: "hello"
输出: "holle"

示例 2:
输入: "leetcode"
输出: "leotcede"

说明:
元音字母不包含字母"y"。
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        yuan_yin = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)

        length = len(s)
        start = 0
        end = length - 1
        while start < end:
            while start < end and s[start] not in yuan_yin:
                start += 1

            while start < end and s[end] not in yuan_yin:
                end -= 1

            s[start], s[end] = s[end], s[start]

            start += 1
            end -= 1

        return ''.join(s)


if __name__ == '__main__':
    S = Solution()
    s = "a."
    print(S.reverseVowels(s))
    