class Solution:
    def binary_search(self, array, target):
        length = len(array)
        start = 0
        end = length - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target < array[mid]:
                end = mid - 1
            elif target > array[mid]:
                start = mid + 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    num = [1,2,3,4,5,6,7]
    S = Solution()
    print(S.binary_search(num, 4))
