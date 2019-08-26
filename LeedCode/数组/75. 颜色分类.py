class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        #         length = len(nums)
        #         count_num = [0, 0, 0]
        #         for i in range(length):
        #             count_num[nums[i]] += 1

        #         index = 0
        #         for n in range(len(count_num)):
        #             for m in range(count_num[n]):
        #                 nums[index] = n
        #                 index += 1
        #         return nums

        length = len(nums)
        zero = -1
        two = length

        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                zero += 1
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
        return nums


if __name__ == '__main__':
    a = [2,0,2,1,1,0]
    s = Solution()
    print(s.sortColors(a))

