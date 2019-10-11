"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""


class Solution:
    # O(n)
    def findKthLargest(self, nums, k):
        length = len(nums)
        kth_min = length - k
        return self.quick_sorted(nums, kth_min, 0, length - 1)

    def quick_sorted(self, array, k, start, end):
        if start > end:
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

        if k > low:
            return self.quick_sorted(array, k, low + 1, end)
        elif k < low:
            return self.quick_sorted(array, k, start, low - 1)
        else:
            return mid


# class Solution:
#     # O(nlog(k))
#     def findKthLargest(self, nums, k):
#         # 维护一个k大小的小顶堆，则堆顶即为第k大的值
#         arr = []
#         for i in range(k):
#             arr.append(nums[i])
#
#         # 调整堆
#         for j in range((len(arr) - 1) // 2, -1, -1):
#             self.heap_adjust(arr, j, len(arr))
#
#         # 当前堆顶存放堆中最小的元素，则当nums[k]大于堆顶时，更新堆顶的元素并调整堆
#         for n in range(k, len(nums)):
#             if nums[n] > arr[0]:
#                 arr[0] = nums[n]
#                 self.heap_adjust(arr, 0, len(arr))
#         return arr[0]
#
#     def heap_adjust(self, arr, index, length):
#         l = 2 * index + 1
#         r = 2 * index + 2
#         if l < length:
#             if r < length and arr[l] > arr[r]:
#                 k = r
#             else:
#                 k = l
#             if arr[index] > arr[k]:
#                 arr[index], arr[k] = arr[k], arr[index]
#                 self.heap_adjust(arr, k, length)


if __name__ == '__main__':
    S = Solution()
    arr = [1,8,3]
    k = 2
    print(S.findKthLargest(arr, k))

