"""
题目描述：
已知字母序列'dgecfboa',请实现一个方法，要求对输入的一组字符串['bed','dog','dear','eye']按照字母顺序排序并打印。本例的输出顺序为：dear,
dog,eye,bed。
"""


class Solution:
    """
    为给定的字母序列建立一个可以进行大小比较的序列，采用map数据结构来实现map的键为给定的字母序列，其值为从0开始依次递增的整数，对于没在字母序列
    中的字母，对应的值统一按-1来处理。
    时间复杂度o(N3)
    空间复杂度O(N)
    """
    def __init__(self, sequeue):
        self.__char2int = {}
        self.build_char2int(sequeue=sequeue)

    def build_char2int(self, sequeue=None):
        if sequeue is None:
            return

        for index, i in enumerate(sequeue):
            self.__char2int[i] = index

    def campare(self, str1, str2):
        if str1 is None and str2 is None:
            return 0

        len1 = len(str1)
        len2 = len(str2)

        i = 0
        j = 0
        while i < len1 and j < len2:
            if str1[i] not in self.__char2int:
                self.__char2int[str1[i]] = -1
            if str2[j] not in self.__char2int:
                self.__char2int[str2[j]] = -1

            if self.__char2int[str1[i]] < self.__char2int[str2[j]]:
                return -1
            elif self.__char2int[str1[i]] > self.__char2int[str2[j]]:
                return 1
            else:
                i += 1
                j += 1

        if i == len1 and j == len2:
            return 0
        elif i == len1:
            return -1
        elif j == len2:
            return 1

    def sorted(self, str):
        length = len(str)
        for i in range(length - 1):
            for j in range(length - 1 - i):
                # print(str[j], str[j + 1])
                if self.campare(str[j], str[j + 1]) == 1:
                    str[j], str[j + 1] = str[j + 1], str[j]
            print(str)


if __name__ == '__main__':
    sequeue = 'dgecfboa'
    string = ['bed', 'dog', 'dear', 'eye']

    S = Solution(sequeue)
    S.sorted(string)
