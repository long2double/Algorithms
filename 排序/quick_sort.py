# 每次找到第一个元素应该在的位置，左侧小于，右侧大于，然后分别递归左侧，和右侧
def quick_sorted(array, start, end):
    """
   最好情况时间复杂度为O(nlogn)
   平均情况时间复杂度为O(nlogn)
   最坏情况时间复杂度为O(n2)
   空间复杂度为O(logn)
   不稳定
   """
    if start >= end:  # 只有左指针小于右指针才进行比较，递归终止条件
        return array

    mid = array[start]   # 每次第一个元素作为所要寻找的位置元素
    low = start
    high = end
    while low < high:  # 只用low<high才进行循环
        while low < high and array[high] > mid:  # high值大于中间值，high向左移动
            high -= 1
        array[low] = array[high]  # 否则，high值给low值

        while low < high and array[low] < mid:  # low值小于中间值，low向右移动
            low += 1
        array[high] = array[low]   # 否则，low值给high值

    array[low] = mid  # 当low=high时退出循环，middle给low值
    quick_sorted(array, start, low - 1)  # 小于middle的值，进行比较
    quick_sorted(array, low + 1, end)  # 大于middle的值，进行比较


if __name__ == '__main__':
    arr0 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sorted(arr0, 0, len(arr0) - 1)
    print(arr0)


