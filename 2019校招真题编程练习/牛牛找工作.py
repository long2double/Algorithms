"""
题目描述
为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
保证不存在两项工作的报酬相同。

输出描述:
对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。
"""


import sys


def main():
    """
    思路:找到难度不大于能力的所有工作里，报酬最多的。核心是用HashMap来记录难度和不超过该难度的最大报酬。
        先把工作的难度和报酬映射到HashMap
        把人的能力也全部读进来，放到HashMap，报酬可以先设为0.
        最后按难度从小到大（所以需要先排序）更新HashMap,key为难度，value为不超过难度的最大报酬。
    """
    lines = sys.stdin.readlines()
    lines = [l.strip().split() for l in lines if l.strip()]

    work_num = int(lines[0][0])
    friend_num = int(lines[0][1])
    res = [0] * (work_num + friend_num)
    power = list(map(int, lines[-1]))

    power_money = {}
    for index, work in enumerate(lines[1:-1]):
        work_hard, money = int(work[0]), int(work[1])
        power_money[work_hard] = money
        res[index] = work_hard

    for index, each_power in enumerate(power):
        res[index + work_num] = each_power
        if each_power not in power_money:
            power_money[each_power] = 0

    res.sort()
    max_salary = 0
    for index, i in enumerate(res):
        max_salary = max(max_salary, power_money[i])
        power_money[res[index]] = max_salary

    for i in power:
        print(power_money[i])


if __name__ == '__main__':
    main()
