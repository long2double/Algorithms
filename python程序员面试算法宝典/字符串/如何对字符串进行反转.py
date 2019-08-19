"""
题目描述：
实现字符串的反转，要求不使用任何系统方法，且时间复杂度最小
"""


class Solution:
    """
    利用异或操作
    a = a^b
    b = a^b = (a^b)^b = a
    a = a^b = (a^b)^a = b
    时间复杂度O(N)
    """
    def reversed(self, string):
        list1 = list(string)

        length = len(string)
        i = 0
        j = length - 1
        while i < j:
            list1[i] = chr(ord(list1[i]) ^ ord(list1[j]))
            list1[j] = chr(ord(list1[i]) ^ ord(list1[j]))
            list1[i] = chr(ord(list1[i]) ^ ord(list1[j]))
            i += 1
            j -= 1
        return ''.join(list1)


if __name__ == '__main__':
    S = Solution()
    print(S.reversed('adfgg'))

