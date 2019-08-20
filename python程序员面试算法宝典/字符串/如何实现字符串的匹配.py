"""
题目描述：
给定主字符串S与模式字符串P，判断P是否是S的子串，如果是，那么找出P在S中第一次出现的下标
"""


class Solution:
    def __init__(self):
        self.__next = None

    def KMP(self, s, p):
        if s is None or p is None:
            return

        self.get_next(p)

        slen = len(s)
        plen = len(p)
        i, j = 0, 0
        while i < slen and j < plen:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = self.__next[j]

        if j == plen:
            return i - j
        else:
            return -1

    def get_next(self, p):
        plen = len(p)

        self.__next = [-1] * plen
        k = -1
        j = 0
        while j < plen - 1:
            if k == -1 or p[j] == p[k]:
                k += 1
                j += 1
                self.__next[j] = k
            else:
                k = self.__next[k]


if __name__ == '__main__':
    s = 'BBC ABCDAB ABCDABABDE'
    p = 'ABCDABA'
    S = Solution()
    print(S.KMP(s, p))



