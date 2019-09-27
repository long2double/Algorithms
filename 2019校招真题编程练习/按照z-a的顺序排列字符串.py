def campare(str1, str2):
    if str1 is None and str2 is None:
        return 0

    len1 = len(str1)
    len2 = len(str2)

    i = 0
    j = 0
    while i < len1 and j < len2:
        if str1[i] > str2[j]:
            return 1
        elif str1[i] < str2[j]:
            return -1
        else:
            i += 1
            j += 1

    if i == len1 and j == len2:
        return 0
    elif i == len1:
        return 1
    elif j == len2:
        return -1


# list_input = input().strip(',')

list_input = 'waimai,dache,lvyou,liren,meishi,jiehun,lvyoujingdian,jiaopei,menpiao,jiudian'.split(',')
list_input = list(list_input)
length = len(list_input)

for i in range(length):
  for j in range(length - i - 1):
    if campare(list_input[j], list_input[j + 1]) == -1:
        list_input[j], list_input[j + 1] = list_input[j + 1], list_input[j]

print(','.join(list_input))