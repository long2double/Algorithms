"""
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
输入："ab-cd"
输出："dc-ba"

示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
 
提示：
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \ or "
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        length = len(s)
        low = 0
        high = length - 1
        S = list(s)
        print(S)
        while low < high:
            while low < high and not S[low].isalpha():
                low += 1
            while low < high and not S[high].isalpha():
                high -= 1
            if low < high:
                S[low], S[high] = S[high], S[low]
                low += 1
                high -= 1
        return ''.join(S)


