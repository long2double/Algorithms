"""
题目描述
牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并且决定起不起床。从他起床算起他需要X分钟到达教室，上课时间为当天的A时B分，请问他最晚可以什么时间起床

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
数据保证至少有一个闹钟可以让牛牛及时到达教室。

输出描述:
输出两个整数表示牛牛最晚起床时间。

示例1
输入
3
5 0
6 0
7 0
59
6 59

输出
6 0
"""


import sys

row_num = int(sys.stdin.readline().strip())
clock_num = [list(map(int, sys.stdin.readline().strip().split())) for i in range(row_num)]
time_cost = int(sys.stdin.readline().strip())
start_h, start_m =list(map(int, sys.stdin.readline().strip().split()))
clock_num.sort()

r_h, r_m = 0, 0
for h, m in clock_num:
    m1 = (m + time_cost) % 60  # 41
    h1 = (m + time_cost) // 60  # 1
    if h + h1 < start_h:
        r_h, r_m = h, m
    elif h + h1 == start_h:
        if m1 <= start_m:
            r_h, r_m = h, m
print(r_h, r_m)