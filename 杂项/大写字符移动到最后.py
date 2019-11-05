"""
把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间
"""


class Solution:
    def move_char(self, str):
        if str is None or str == '':
            return

        list1 = list(str)
        length = len(list1)
        for i in range(1, length):
            j = i
            if 'a' <= list1[i] <= 'z':
                while j != 0 and 'A' <= list1[j - 1] <= 'Z':
                    list1[j - 1], list1[j] = list1[j], list1[j - 1]
                    j -= 1
                print('++', ''.join(list1))
        return ''.join(list1)


if __name__ == '__main__':
    S = Solution()
    array = "PynILoveYoUdfs"
    print(S.move_char(array))