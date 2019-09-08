def generate(item, n, result):
    if len(item) == 2 * n:
        result.append(item)
        return

    generate(item + '(', n , result)
    generate(item + ')', n, result)


if __name__ == '__main__':
    result = []
    generate('', 2, result)
    for i in range(len(result)):
        print(''.join(result[i]))
