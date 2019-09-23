class Solution:
    def multiply(self, A):
        # write code here
        a = [1]
        b = [1]
        res = []
        for i in range(len(A)):
            a.append(a[i] * A[i])
            b.append(b[i] * A[len(A) - 1 - i])

        for j in range(len(A)):
            res.append(a[j] * b[len(A) - 1 - j])
        return res


if __name__ == '__main__':
    S = Solution()
    num = [1, 2, 3, 4, 5]
    print(S.multiply(num))
