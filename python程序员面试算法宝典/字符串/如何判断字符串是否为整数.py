"""
题目描述：
写一个方法，检查字符串是否是整数，如果是整数，那么返回其整数值
"""


class Solution:
    """
    首先判断字符是否符合整数的要求，即除了第一位外可能是符号位，可能是0~9或-，+，其余的只能是0~9。然后，从后往前组合整数
    时间复杂度O(N)
    空间复杂度O(1)
    """
    def ConvertStr2Int(self, string):
        if string is None:
            return

        if string[0] != '-' and string[0] != '+' and string[0] < '0' and string[0] > '9':
            return

        sums = 0
        for index, s in enumerate(string[::-1]):
            if index < len(string) - 1:
                if s < '0' or s > '9':
                    return

            if s == '-':
                return -sums
            if s == '+':
                return sums
            sums += (ord(s) - ord('0')) * 10 ** index
        return sums


if __name__ == '__main__':
    string = '-543'
    S = Solution()
    print(S.ConvertStr2Int(string))
