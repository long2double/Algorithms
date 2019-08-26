# 堆通常指的是一颗完全二叉树
def heap_sorted(array):
    length = len(array)
    # 创建小根堆
    for i in range((length - 1) // 2, -1, -1):
        adjust_heap(array, i, length)
        #print(array)  # 初始堆的情况

    # 堆排序
    for j in range(length - 1, -1, -1):
        array[0], array[j] = array[j], array[0]
        adjust_heap(array, 0, j)


# 创建的是大根堆，输出的是升序，因为调整的时候，需要将父结点至于数组尾部
def adjust_heap(array, index, length):
    lchild = 2 * index + 1
    rchild = 2 * index + 2
    if lchild < length:
        if rchild < length and array[rchild] > array[lchild]:
            k = rchild
        else:
            k = lchild

        if array[index] < array[k]:
            array[index], array[k] = array[k], array[index]
            adjust_heap(array, k, length)


if __name__ == '__main__':
    # arr0 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    arr0 = [5, 11, 7, 2, 3, 17]
    heap_sorted(arr0)
    print(arr0)
