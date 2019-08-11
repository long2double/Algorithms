# 每次比较相邻的值，一次寻找出的是最大值
def bubble_sorted(array):
    """
    最好情况时间复杂度为O(n)
    平均情况时间复杂度为O(n2)
    最坏情况时间复杂度为O(n2)
    空间复杂度为O(1)
    稳定
    """
    length = len(array)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble_sorted_k(array, k):
    length = len(array)
    for i in range(length):  # 前k小的需要全比较
        for j in range(length - 1 - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        if i == k - 1:
            return array[-k]


if __name__ == '__main__':
    arr0 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sorted(arr0)
    print(arr0)

    arr1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(bubble_sorted_k(arr1, 5))

