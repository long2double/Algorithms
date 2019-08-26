"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''
        for i in s:
            if i.isalnum():
                tmp += i.lower()
        print(tmp)
        length = len(tmp)
        start = 0
        end = length - 1
        while start < end:
            if tmp[start] == tmp[end]:
                start += 1
                end -= 1
            else:
                print('==')

                return False
        return True


if __name__ == '__main__':
    S = Solution()
    arr = "A man, a plan, a canal: Panama"
    print(S.isPalindrome(arr))