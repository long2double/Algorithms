arr = "Python UdfsRdf"
arr = list(arr)
for index, value in enumerate(arr):
    if 'A' <= value <= 'Z':
        tem = arr.pop(index)
        print(tem)
        arr.append(tem)


print(''.join(arr))