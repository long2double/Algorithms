# 分而治之，先整个数组分到最小，然后按照大小组合数组
def merger_sorted(array):
    """
    最好情况时间复杂度为O(nlogn)
    平均情况时间复杂度为O(nlogn)
    最坏情况时间复杂度为O(nlogn)
    空间复杂度为O(n)
    稳定
    """
    n = len(array)
    if n <= 1:
        return array

    mid = n // 2
    left = merger_sorted(array[:mid])
    right = merger_sorted(array[mid:])

    res = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            res.append(left[left_pointer])
            left_pointer += 1
        else:
            res.append(right[right_pointer])
            right_pointer += 1

    res += left[left_pointer:]
    res += right[right_pointer:]

    return res


if __name__ == '__main__':
    arr0 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merger_sorted(arr0))
