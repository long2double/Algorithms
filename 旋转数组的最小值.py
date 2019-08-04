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
