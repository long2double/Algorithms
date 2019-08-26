def compare1(str1, str2):
    num = 0
    i = 0
    length1 = len(str1)
    length2 = len(str2)
    while i < length1 and i < length2:
        if str1[i] == str2[i]:
            num += 1
        else:
            break
        i += 1
    return num


def main():
    """
    3
    1 2
    2 3
    abcvd
    abdfrw
    abdf
    """
    num = int(input())
    string = []
    for i in range(num):
        string.append(input())
    for j in range(num - 1):
        a, b = list(map(int, input().split()))
        str1 = string[a - 1]
        str2 = string[b - 1]

        number = compare1(str1, str2)
        print(number)


if __name__ == '__main__':
    main()

