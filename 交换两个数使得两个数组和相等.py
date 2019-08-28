class Solution:
    def swap(self, arr1, arr2):
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        mid = (sum1 + sum2) // 2
        res = []
        for i in arr1:
            ret = mid - (sum1 - i)
            if ret in arr2:
                res.append([i, ret])
        return res


if __name__ == '__main__':
    arr1 = [1,2,3]
    arr2 = [2, 2, 4]
    S = Solution()
    print(S.swap(arr1, arr2))

