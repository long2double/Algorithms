"""
题目描述：
找到两个字符串的最长公共子串，例如str1='abccade',str2='dfcadde'的最长公共子串为'cad'
"""


class Solution:
    """
    动态规划：
          d, g, c, a, d, d, e
       0, 0, 0, 0, 0, 0, 0, 0
     a 0, 0, 0, 0, 1, 0, 0, 0
     b 0, 0, 0, 0, 0, 0, 0, 0
     c 0, 0, 0, 1, 0, 0, 0, 0
     c 0, 0, 0, 1, 0, 0, 0, 0
     a 0, 0, 0, 0, 2, 0, 0, 0
     d 0, 0, 0, 0, 0, 3, 1, 0
     e 0, 0, 0, 0, 0, 0, 0, 2
     时间复杂度O(n * m)
     空间复杂度O(n * m)
    """

    def maxSubStr(self, str1, str2):
        list1 = list(str1)
        list2 = list(str2)
        length1 = len(list1)
        length2 = len(list2)

        M = [[0] * (length2 + 1) for i in range(length1 + 1)]  # 6 7

        maxs = 0
        max_index = 0
        for n in range(1, length1 + 1):
            for m in range(1, length2 + 1):
                if list1[n - 1] == list2[m - 1]:
                    M[n][m] = M[n - 1][m - 1] + 1
                    if M[n][m] > maxs:
                        maxs = M[n][m]
                        max_index = n

        return ''.join(list1[max_index - maxs:max_index])


if __name__ == '__main__':
    a = 'abccade'
    b = 'dfcadde'
    S = Solution()
    print(S.maxSubStr(a, b))
