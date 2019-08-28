def water(n):
    i = 0
    sums = 0
    while i < n:
        sums += 1 / (2 ** i)
        i += 1
    return sums


def water_(n, sums):
    if n == 0:
        return float.as_integer_ratio(sums)
    sums += 1 / (2 ** (n - 1))
    return water_(n - 1, sums)


if __name__ == '__main__':
    print(water(4))
    print(water_(4, 0))
