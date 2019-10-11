"""
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


# -*- coding:utf-8 -*-
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         # write code here
#         length = len(tinput)
#         if k > length or k == 0:
#             return []
#         res = []
#         for i in range(length):
#             min = i
#             for j in range(i + 1, length):
#                 if tinput[j] < tinput[min]:
#                     min = j
#             tinput[i], tinput[min] = tinput[min], tinput[i]
#             res.append(tinput[i])
#             if len(res) == k:
#                 return res


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        length = len(tinput)
        if k == 0 or k > length:
            return []

        res = []
        for i in range(1, k + 1):
            kth = length - i
            res.append(self.quick_sorted(tinput, kth, 0, length - 1))
        return res

    def quick_sorted(self, array, kth, start, end):
        if start > end:
            return array

        mid = array[start]
        low = start
        high = end
        while low < high:
            while low < high and array[high] <= mid:
                high -= 1
            array[low] = array[high]

            while low < high and array[low] > mid:
                low += 1
            array[high] = array[low]
        array[low] = mid

        if kth > low:
            return self.quick_sorted(array, kth, low + 1, end)
        elif kth < low:
            return self.quick_sorted(array, kth, start, low - 1)
        else:
            return mid


# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k == 0:
            return []
        num = []
        for i in range(k):
            num.append(tinput[i])
        for j in range((len(num) // 2 - 1), -1, -1):
            self.heap_adjust(num, j, len(num))

        for n in range(i + 1, len(tinput)):
            if tinput[n] < num[0]:
                num[0] = tinput[n]
                self.heap_adjust(num, 0, k)

        for m in range(len(num) - 1, -1, -1):
            num[0], num[m] = num[m], num[0]
            self.heap_adjust(num, 0, m)
        return num

    def heap_adjust(self, array, index, length):
        l = 2 * index + 1
        r = 2 * index + 2
        if l < length:
            if r < length and array[l] < array[r]:
                k = r
            else:
                k = l

            if array[index] < array[k]:
                array[index], array[k] = array[k], array[index]
                self.heap_adjust(array, k, length)


if __name__ == '__main__':
    S = Solution()
    array = [1,8,3,9,7,2,0]
    # S.GetLeastNumbers_Solution(array, 4)

    print(S.GetLeastNumbers_Solution(array, 6))
    print(array)

