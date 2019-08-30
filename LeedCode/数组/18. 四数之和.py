"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值
与 target 相等？找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        res = []
        if nums == []:
            return []

        nums.sort()
        length = len(nums)
        for a in range(length - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            new_tar1 = target - nums[a]

            for b in range(a + 1, length - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                new_tar2 = new_tar1 - nums[b]
                c, d = b + 1, length - 1
                while c < d:
                    if nums[c] + nums[d] == new_tar2:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1
                    elif nums[c] + nums[d] < new_tar2:
                        c += 1
                    else:
                        d -= 1
        return res


if __name__ == '__main__':
    S = Solution()
    s = [-4, -1, -1, 0, 1, 2]
    target = -1
    print(S.fourSum(s, target))
