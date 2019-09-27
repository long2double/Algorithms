"""
//假设交换后的差值是diff_after,则交换后
suma(交换后) = suma(交换前) - a[i] + b[j]
sumb(交换后) = sumb(交换前) - b[j] + a[i]
//两个等式相减可得:
diff_after = (suma (交换前)  - sumb (交换前) ) - 2( a[i] - b[j])
           = diff - 2(a[i] - b[j])
//交换后的绝对值小于交换前,也就是abs(diff_after) < abs(diff_before)
"""


def exchange(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    diff_before = abs(sum1 - sum2)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            sum1 = sum1 - arr1[i] + arr2[j]
            sum2 = sum2 - arr2[j] + arr1[i]
            diff_after = abs(sum1 - sum2)
            if diff_after < diff_before:
                arr1[i], arr2[j] = arr2[j], arr1[i]
                exchange(arr1, arr2)
                # return arr1, arr2


if __name__ == '__main__':
    arr1 = [1,2, 3]
    arr2 = [1, 1, 2]
    exchange(arr1, arr2)
    print(arr1, arr2)
