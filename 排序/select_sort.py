# 每次找到后续的最小值索引，与当前的外层循环的值交换
def select_sorted(array):
    """
    最好情况时间复杂度为O(n2)
    平均情况时间复杂度为O(n2)
    最坏情况时间复杂度为O(n2)
    空间复杂度为O(1)
    不稳定
    """
    length = len(array)
    for i in range(length - 1):
        min = i
        for j in range(i + 1, length):
            if array[j] < array[min]:
                min = j
        array[min], array[i] = array[i], array[min]


def select_sorted_k(array, k):
    length = len(array)
    for i in range(length):  # 前k小的要全比较
        min = i
        for j in range(i + 1, length):
            if array[j] < array[min]:
                min = j
        array[min], array[i] = array[i], array[min]
        if i == k - 1:
            return array[i]


if __name__ == '__main__':
    arr0 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    select_sorted(arr0)
    print(arr0)

    arr1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(select_sorted_k(arr1, 4))
