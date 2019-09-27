class Solution:
    def binary_search(self, array, start, end, target):
        if start > end:
            return -1
        mid = start + (end - start) // 2
        if target < array[mid]:
            return self.binary_search(array, start, mid - 1, target)
        elif target > array[mid]:
            return self.binary_search(array, mid + 1, end, target)
        else:
            return mid


if __name__ == '__main__':
    num = [1,2,3,4,5,6,7]
    S = Solution()
    print(S.binary_search(num, 0, len(num) - 1, 4))
