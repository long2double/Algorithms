# 当前元素从索引1开始与前面有序的数列，从后往前进行比较
def insert_sorted(array):
    """
    最好情况时间复杂度为O(n)
    平均情况时间复杂度为O(n2)
    最坏情况时间复杂度为O(n2)
    空间复杂度为O(1)
    稳定
    """
    length = len(array)

    for i in range(length - 1):
        for j in range(i + 1, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array


if __name__ == '__main__':
    arr0 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(insert_sorted(arr0))
