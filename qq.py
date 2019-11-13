class Solution:
    def __init__(self):
        self.sub = []
        self.res = [[]]
        
    def per(self, array):
        if array is None or len(array) == 0:
            return self.res

        self.find_sub(array, 0)
        return self.res

    def find_sub(self, array, i):
        if i == len(array):
            return

        self.sub.append(array[i])
        self.res.append(self.sub[:])
        self.find_sub(array, i + 1)
        self.sub.pop()
        self.find_sub(array, i + 1)


if __name__ == '__main__':
    array = [1, 2, 3]
    S = Solution()

    print(S.per(array))