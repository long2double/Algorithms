"""
题目描述：
有一个由大小写字母组成的字符串，请对它进行重新组合，使得其中的所有小写字母排在大写字母的前面（大写字母或小写字母之间不要求保持原来的次序）
"""


class Solution:
    """
    可以使用类似快速排序的方法处理，引用两个索引分别指向字符串的首和尾，首索引正向遍历字符串，找到第一个大写字母，尾索引逆向遍历字符串，找
    到第一个小写字母，交换两个索引位置的字符，然后再将两个索引沿着相应的方向继续向前移动，重复上述步骤，直到首索引大于或等于尾索引为止
    """
    def ReverseArray(self, str):
        list1 = list(str)
        low = 0
        high = len(str) - 1

        while low < high:
            while low < high and 'a' <= list1[low] <= 'z':
                low += 1

            while low < high and 'A' <= list1[high] <= 'Z':
                high -= 1

            list1[low], list1[high] = list1[high], list1[low]
        return ''.join(list1)


if __name__ == '__main__':
    string = 'UasASfdskASFwEJ'
    S = Solution()
    print(S.ReverseArray(string))
