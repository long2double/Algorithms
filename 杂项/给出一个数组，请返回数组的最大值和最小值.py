"""
有一个算法，查找n个元素的的数组的最大值和最小值，要比较2n次；请写一个最高效的算法，并说明他要比较的次数。请注意复杂度的常数
(不用写代码，说明步骤和过程即可，要定出比较的次数，没写不给分)
"""


class Solution:
    """
    先遍历一遍数组，两个两个分成一组，小的放在左边大的放在右边，这样比较次数是N/2。N是数组的长度。然后最小的元素一定是在每组的左边，最大的
    元素在右边。下一步在左边的所有元素中比较N/2次产生最小的，在右边的元素中比较N/2次产生最大的。总共需要比较的次数是3*（N/2）次。
    """
    def find_max_min_value(self, array):
        length = len(array)
        if length < 2:
            return

        # 对数组两两进行分组，小的放在左侧，大的放在右侧
        for i in range(0, length - 1, 2):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        # 寻找每组左侧的最小值，即为数组的最小值
        min = array[0]
        for i in range(0, length - 1, 2):
            if min > array[i]:
                min = array[i]

        # 寻找每组右侧的最大值，即为数组的最大值
        max = array[1]
        for i in range(1, length - 1, 2):
            if max < array[i]:
                max = array[i]

        # 如果数组为奇数个，单独判断最后一个元素
        if length % 2 == 1:
            if min > array[-1]:
                min = array[-1]
            if max < array[-1]:
                max = array[-1]

        return max, min


if __name__ == '__main__':
    S = Solution()
    array = [0, 4, -1]
    print(S.find_max_min_value(array))

