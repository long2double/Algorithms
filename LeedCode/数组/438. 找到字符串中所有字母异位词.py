"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例 1:
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

示例 2:
输入:
s: "abab" p: "ab"
输出:
[0, 1, 2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
"""


class Solution:
    def findAnagrams(self, s: str, p: str):
        len_p = len(p)
        hasmap_p = {}
        for value in p:
            if value not in hasmap_p:
                hasmap_p[value] = 1
            else:
                hasmap_p[value] += 1

        res = []
        hasmap_s = {}
        for index, value in enumerate(s):
            # 保存每次滑动窗口的哈希值
            if value not in hasmap_s:
                hasmap_s[value] = 1
            else:
                hasmap_s[value] += 1

            # 如果当前窗口的值与p的哈希值相同，则将初始索引加入到res
            if hasmap_s == hasmap_p:
                res.append(index - len_p + 1)
            
            # 只要索引值大于p的长度，则不管窗口是否匹配都需将最后一次的索引对应的值减1
            if index - len_p + 1 >= 0:
                hasmap_s[s[index - len_p + 1]] -= 1
                if hasmap_s[s[index - len_p + 1]] == 0:
                    del hasmap_s[s[index - len_p + 1]]
        return res


if __name__ == '__main__':
    S = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(S.findAnagrams(s, p))
