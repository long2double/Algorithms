import sys

# import sys
#
# course_time, awake_time = list(map(int, sys.stdin.readline().strip().split()))  # 6 3
# awake = list(map(int, sys.stdin.readline().strip().split()))  # 1 3 5 2 5 4
# sorce = list(map(int, sys.stdin.readline().strip().split()))  # 1 1 0 1 0 0
# course_time, awake_time = 6, 3
# course_time, awake_time = 20, 3
# awake = list(map(int, [1, 3, 5, 2, 5, 4]))
# sorce = list(map(int, [1, 1, 0, 1, 0, 0]))

# awake = list(map(int, [7671, 1710, 3898, 2147, 7451, 7607 ,7069, 8984, 5614, 1284 ,7274, 4168, 4317, 5432, 523, 1117 ,5245, 3378, 8196, 368]))
# sorce = list(map(int, [0,     1,     0,   0,     0,    1,    1,    1,    1,    1,    0,    1,    1,    1,    1,  0,    1,    0,     1,   0]))
# sorce_awake = list(zip(sorce, awake))
#
# res = []
# i = 0
# max = -2 ** 32
# while i < course_time:
#     if sorce_awake[i][0] == 1:
#         res.append(sorce_awake[i][1])
#         i += 1
#     elif sorce_awake[i][0] == 0:
#         j = 0
#         while j < awake_time and i + j < course_time:
#             res.append(sorce_awake[i + j][1])
#             j += 1
#         post = 0
#         num = 0
#         while i + j + post < course_time:
#             if sorce_awake[i + j + post][0] == 1:
#                 res.append(sorce_awake[i + j + post][1])
#                 num += 1
#             post += 1
#
#         if sum(res) > max:
#             max = sum(res)
#
#         fin = j + num
#         while fin > 0:
#             res.pop()
#             fin -= 1
#         i += 1
#
# print(max)

# course_time, awake_time = 20, 3
# awake = list(map(int, [7671, 1710, 3898, 2147, 7451, 7607 ,7069, 8984, 5614, 1284 ,7274, 4168, 4317, 5432, 523, 1117 ,5245, 3378, 8196, 368]))
# sorce = list(map(int, [0,     1,     0,   0,     0,    1,    1,    1,    1,    1,    0,    1,    1,    1,    1,  0,    1,    0,     1,   0]))

# course_time, awake_time = 10, 5
# awake = list(map(int, [6481, 6127, 4477, 5436, 7356, 3137, 1076, 7182, 8147, 835]))
# sorce = list(map(int, [1,     0,    1,     0,    1,    1,   0,     0,    0,   1]))
# sorce_awake = list(zip(sorce, awake))
#
# sums = 0
# for sorce_, awake_ in sorce_awake:
#     if sorce_ == 1:
#         sums += awake_
# sums_tmp = sums
#
# i = 0
# max = -2 * 32
#
# while i < course_time:
#     j = 0
#     if sorce_awake[i][0] == 0:
#         while j < awake_time and j + i < course_time:
#             if sorce_awake[i + j][0] == 0:
#                 print(i + j)
#                 print("sorce_awake[i][1]",  sorce_awake[i + j][1])
#                 sums_tmp += sorce_awake[i + j][1]
#             j += 1
#
#         if sums_tmp > max:
#             max = sums_tmp
#         sums_tmp = sums
#     i += 1
# print(max)


# course_time, awake_time = 20, 3
# awake = list(map(int, [7671, 1710, 3898, 2147, 7451, 7607 ,7069, 8984, 5614, 1284 ,7274, 4168, 4317, 5432, 523, 1117 ,5245, 3378, 8196, 368]))
# sorce = list(map(int, [0,     1,     0,   0,     0,    1,    1,    1,    1,    1,    0,    1,    1,    1,    1,  0,    1,    0,     1,   0]))

course_time, awake_time = 10, 5
awake = list(map(int, [6481, 6127, 4477, 5436, 7356, 3137, 1076, 7182, 8147, 835]))
sorce = list(map(int, [1,     0,    1,     0,    1,    1,   0,     0,    0,   1]))
sorce_awake = list(zip(sorce, awake))

sums = 0
sorce_li = []
for index, value in enumerate(sorce_awake):
    if value[0] == 1:
        sums += value[1]
        if len(sorce_li) == 0:
            sorce_li.append(0)
        else:
            sorce_li.append(sorce_li[-1])
    else:
        if len(sorce_li) == 0:
            sorce_li.append(value[1])
        else:
            sorce_li.append(sorce_li[-1] + value[1])

sums_tmp = sums
# [(1, 0), (0, 6127), (1, 6127), (0, 11563), (1, 11563), (1, 11563), (0, 12639), (0, 19821), (0, 27968), (1, 27968)]
sorce_awake_1 = list(zip(sorce, sorce_li))
max = -2 ** 32
for index, (sorce_, awake_) in enumerate(sorce_awake_1):
    if sorce_ == 1:
        if sums_tmp > max:
            max = sums_tmp
    else:
        i = index + awake_time - 1
        if index == 0:
            sums_tmp += sorce_awake_1[i][1]
        elif i < course_time:
            tmp = sorce_awake_1[i][1] - sorce_awake_1[index - 1][1]
            sums_tmp += tmp
        else:
            sums_tmp += sorce_awake_1[-1][1] - sorce_awake_1[index - 1][1]
        if sums_tmp > max:
            max = sums_tmp
        sums_tmp = sums

print(max)