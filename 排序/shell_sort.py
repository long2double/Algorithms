def shell_sorted(array, k):
    """
    最好情况时间复杂度为O(n1.3)
    平均情况时间复杂度为O(nlogn)
    最坏情况时间复杂度为O(n2)
    空间复杂度为O(1)
    不稳定
    """
    length = len(array)
    gap = k
    while gap > 0:
        for i in range(length - gap):
            for j in range(i + gap, gap - 1, -gap):
                if array[j] < array[j - gap]:
                    array[j], array[j - gap] = array[j - gap], array[j]
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    arr0 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sorted(arr0, 8)
    print(arr0)
