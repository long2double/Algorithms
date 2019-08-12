"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # if rotateArray == []:
        # return 0
        # length = len(rotateArray)
        # for i in range(length - 1):
        # if rotateArray[i] > rotateArray[i + 1]:
        # return rotateArray[i + 1]
        # return rotateArray[0]
        return self.findMin(rotateArray, 0, len(rotateArray) - 1)

    def findMin(self, rotateArray, low, high):
        if low > high:
            return 0
        mid = (low + high) // 2

        if rotateArray[mid] > rotateArray[mid + 1]:
            return rotateArray[mid + 1]
        elif rotateArray[mid] < rotateArray[mid - 1]:
            return rotateArray[mid]
        elif rotateArray[mid] > rotateArray[low]:
            return self.findMin(rotateArray, mid + 1, high)
        elif rotateArray[mid] < rotateArray[low]:
            return self.findMin(rotateArray, low, mid - 1)
        elif rotateArray[mid] == rotateArray[low] and rotateArray[mid] == rotateArray[high]:
            return min(self.findMin(rotateArray, low, mid - 1), self.findMin(rotateArray, mid + 1, high))
