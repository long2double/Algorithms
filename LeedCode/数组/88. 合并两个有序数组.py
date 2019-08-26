class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        if n != 0:
            ptr12 = m + n - 1  # 1
            ptr1 = m - 1
            ptr2 = n - 1
            while ptr1 >= 0 and ptr2 >= 0:
                if nums1[ptr1] <= nums2[ptr2]:
                    nums1[ptr12] = nums2[ptr2]
                    ptr12 -= 1
                    ptr2 -= 1
                else:
                    nums1[ptr12] = nums1[ptr1]
                    ptr12 -= 1
                    ptr1 -= 1

            if ptr1 < 0 and ptr2 >= 0:
                nums1[:ptr2 + 1] = nums2[:ptr2 + 1]
            return nums1


if __name__ == '__main__':
    nums1 = [1, 0]
    m = 1
    nums2 = [2]
    n = 1
    S = Solution()
    print(S.merge(nums1, m, nums2, n))



