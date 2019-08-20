"""
题目描述：
给定一个如下格式的字符串：'(1,(2,3),(4,(5,6),7))'，括号内的元素可以是数字，也可以是另外一个括号，实现一个算法消除嵌套的括号，例如把上面
的表达式变成(1,2,3,4,5,6,7)，如果表达式有误，那么返回False
时间复杂度O(N)
空间复杂度O(N)
"""


class Solution:
    """
    碰到'('，把括号的计数器的值加上1，碰到')'，把括号的计数器的值减去1。最后判断计数器的是否为0，为0则正确的表达式，否则，不是。
    """
    def removeNestedPare(self, string):
        if string[0] != '(' and string[-1] != ')':
            return False

        res = '('
        count = 0
        for i in string[1:-1]:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            else:
                res += i

        if count != 0:
            return False

        res += ')'
        return res


if __name__ == '__main__':
    string = '(1,(2,3),(4,(5,6),7))'
    S = Solution()
    print(S.removeNestedPare(string))
