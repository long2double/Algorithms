"""
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例 4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false

说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
"""


class Solution:
    def wordPattern(self, pattern, str):
        list_str = str.split()
        len_p = len(pattern)
        len_s = len(list_str)

        if len_p != len_s:
            return False

        has_map = {}
        has_use = {}
        for i in range(len_p):
            if pattern[i] not in has_map:
                if list_str[i] in has_use:
                    return False
                has_map[pattern[i]] = list_str[i]
                has_use[list_str[i]] = True
            else:
                if has_map[pattern[i]] != list_str[i]:
                    return False
        return True


if __name__ == '__main__':
    p = "abba"
    str = "dog cat cat dog"
    S = Solution()
    print(S.wordPattern(p, str))


