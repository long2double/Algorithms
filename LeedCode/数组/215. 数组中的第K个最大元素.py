class Solution:
    def __init__(self):
        self.index = 0

    def findKthLargest(self, nums, k):
        length = len(nums)
        kth_min = length - k + 1
        self.quick_sorted(nums, 0, length - 1, kth_min)

    def quick_sorted(self, array, start, end, k):
        if start >= end:
            return array

        mid = array[start]
        low = start
        high = end
        while low < high:
            while low < high and array[high] >= mid:
                high -= 1
            array[low] = array[high]

            while low < high and array[low] < mid:
                low += 1
            array[high] = array[low]

            array[low] = mid
            print(low)
            if k - 1 > low:
                self.quick_sorted(array, low + 1, end, k)
            elif k - 1 < low:
                self.quick_sorted(array, start, low - 1, k)
            else:
                self.index = low
            # self.quick_sorted(array, low + 1, end, k)
            # self.quick_sorted(array, start, low - 1, k)


S = Solution()
arr0 = [-1,2,0]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
S.findKthLargest(arr0, 2)
# S.quick_sorted(arr0, 0 , 2, 2)
# print(arr0)
# print(S.index)
# print(arr0[S.index])