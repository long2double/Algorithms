# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum == 1:
            return []

        array = []
        for i in range(1, tsum):
            array.append(i)
        start = 0
        end = 1
        res = []
        while start < end:
            if sum(array[start:end]) < tsum:
                end += 1
            elif sum(array[start:end]) > tsum:
                start += 1
            else:
                res.append(array[start: end])
                end += 1
                start += 1
            if end > tsum // 2 + 1:
                break
        return res


if __name__ == '__main__':
    S = Solution()
    num = 3
    print(S.FindContinuousSequence(num))
