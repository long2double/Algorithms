class Solution:
    def sums1(self, arr, sum):
        start = 0
        end = len(arr) - 1
        arr.sort()
        while start < end:
            if arr[start] + arr[end] == sum:
                return arr[start], arr[end]  # 返回索引的值
            elif arr[start] + arr[end] < sum:
                start += 1
            elif arr[start] + arr[end] > sum:
                end -= 1

    def sums2(self, arr, sum):
        hash_map = {}
        for index, i in enumerate(arr):
            if sum - i in hash_map:
                return hash_map[sum - i], index  # 返回索引
            else:
                hash_map[i] = index


if __name__ == '__main__':
    arr = [2, 7, 3, 10, 5]
    S = Solution()
    print(S.sums2(arr, 13))