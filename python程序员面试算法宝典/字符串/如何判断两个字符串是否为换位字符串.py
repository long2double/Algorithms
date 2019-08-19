"""
题目描述：
换位字符串是指组成字符串的字符相同，但位置不同。例如：由于字符串'aaaabc'与字符串'abcbaaa'是由相同的字符所组成的，所以他们是换位字符串
"""


class Solution:
    """
    假设字符中只是使用ASCII字符，由于ASCII字符共有256个（对应的编码为0~255），在实现的时候可以通过申请大小为256的数组来记录每个字符出
    现的个数，并将其初始为0。然后遍历第一个字符串，将字符对应的ASCII码值作为数组下标，把对应数组的元素值加1.然后遍历第二个字符串，把数组
    中对应的元素值减1.如果最后数组中各个元素的值都为0，那么说明这两个字符串是有相同的字符所组成的，否则，不是。
    时间复杂度为O(N)
    空间复杂度为O(256)
    """

    def compare(self, s1, s2):
        if s1 == s2:
            return False
        map_list = [0] * 256
        for i in s1:
            map_list[ord(i)] += 1

        for j in s2:
            map_list[ord(j)] -= 1

        for k in map_list:
            if k != 0:
                return False
        return True


if __name__ == '__main__':
    s1 = 'asdgf'
    s2 = 'asdfg'
    S = Solution()
    print(S.compare(s1, s2))
