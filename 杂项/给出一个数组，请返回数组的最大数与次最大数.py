"""给出一个数组，请返回数组的最大数与次最大数"""


class Solution:
    def bubble_max_num(self, array):
        """ O(nk) """
        res = []
        length = len(array)
        for i in range(length):
            for j in range(length - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            if i <= 1:
                res.append(array[length - 1 - i])
                if i == 1:
                    break
        return res

    def heap_max_num(self, array):
        """ O(nlogk) """
        num = [array[0], array[1]]
        for i in range((len(num) - 1) // 2, -1, -1):
            self.heap_adjust(array, i, len(num))

        for j in range(2, len(array)):
            if array[j] > num[0]:
                num[0] = array[j]
                self.heap_adjust(num, 0, len(num))
        return num[::-1]

    def heap_adjust(self, array, index, length):
        left = 2 * index + 1
        right = 2 * index + 2
        if left < length:
            if right < length and array[right] < array[left]:
                k = right
            else:
                k = left

            if array[index] > array[k]:
                array[index], array[k] = array[k], array[index]
                self.heap_adjust(array, k, length)

    def ptr_max_num(self, array):
        """ O(n) """
        max1_ptr = array[0]
        max2_ptr = array[1]
        for i in range(2, len(array)):
            if array[i] > max1_ptr:
                max2_ptr = max1_ptr
                max1_ptr = array[i]
            elif array[i] > max2_ptr:
                max2_ptr = array[i]
        return [max1_ptr, max2_ptr]


if __name__ == '__main__':
    S = Solution()
    array = [100, 2, 3, 4, 1, 6, -1, 8, 3, 29, 90, 9, 10]
    print(S.bubble_max_num(array))
    print(S.heap_max_num((array)))
    print(S.ptr_max_num(array))





