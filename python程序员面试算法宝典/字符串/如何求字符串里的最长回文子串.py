"""
题目描述：
回文字符串是指一个字符串从左到右与从右到左遍历得到的序列是相同的。例如：'abcba'就是回文字符串，而'abcab'则不是回文字符串
"""


class Solution:
    """
    中心扩展法
    从字符串最中间的字符开始向两边扩展，通过比较左右两边字符是否相等就可以确定这个字符串是否为回文字符串。这种方法对于字符串长度为奇数和
    偶数的情况需要分开处理。例如：'aba'，就可以从最中间的位置'b'开始向两边扩展，但是对于'baab'，就需要从中间的两个字母开始分别向左右两
    边扩展
    """
    def __init__(self):
        self.max_start = 0
        self.max_len = 0

    def longestPalindrome(self, string):
        if string is None or string == []:
            return 0

        length = len(string)
        for i in range(length):
            self.extend(string, i, i, length)
            self.extend(string, i, i + 1, length)

        return self.max_start, self.max_len

    def extend(self, string, left_ptr, right_ptr, length):
        while 0 <= left_ptr <= right_ptr < length:
            if string[left_ptr] == string[right_ptr]:
                tmp_len = right_ptr - left_ptr + 1
                if tmp_len > self.max_len:
                    self.max_len = tmp_len
                    self.max_start = left_ptr
                left_ptr -= 1
                right_ptr += 1
            else:
                break


if __name__ == '__main__':
    string = 'ab0c0ba jk0b ab0cc0ba i'
    S = Solution()
    print(S.longestPalindrome(string))
