# class Solution:
#     def mergy_array(self, num1, num2):
#         length1 = len(num1)
#         length2 = len(num2)
#         n1, n2 = 0, 0
#         res = []
#         while n1 < length1 and n2 < length2:
#             if num1[n1] <= num2[n2]:
#                 res.append(num1[n1])
#                 n1 += 1
#             else:
#                 res.append(num2[n2])
#                 n2 += 1
#
#         res += num1[n1:]
#         res += num2[n2:]
#         return res


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def mergy_array(self, num1, num2):
        length1 = len(num1)
        length2 = len(num2)
        num = [0] * (length1 + length2)
        n1 = length1 - 1
        n2 = length2 - 1
        n = length1 + length2 - 1
        while n1 >= 0 and n2 >= 0:
            if num1[n1] > num2[n2]:
                num[n] = num1[n1]
                n -= 1
                n1 -= 1
            else:
                num[n] = num2[n2]
                n -= 1
                n2 -= 1
        num[:n + 1] = num1[:n1 + 1]
        num[:n + 1] = num2[:n2 + 1]
        return num


if __name__ == '__main__':
    num1 = [1, 3, 6, 7, 10]
    num2 = [2, 4, 8, 11, 22]
    S = Solution()
    print(S.mergy_array(num1, num2))

