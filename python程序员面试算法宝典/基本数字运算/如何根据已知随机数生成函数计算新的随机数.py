"""
题目描述:
已知随机数生成函数rand7()能产生的随机数是整数1~7的均匀分布，如何构造rand10()函数，使其产生的随机数是整数1~10的均匀分布。
"""


import numpy as np


class Solution:
    """
    rand7()产生1~7的随机数，则rand7() - 1产生0~6的随机数。(rand7() - 1）* 7 产生[0, 7, 14, 21, 28, 35, 42],
    (rand7() - 1）* 7 + rand7() 产生[1, 2, 3, 4 ---- , 49],每个数的概率为1/49，依据是均匀的分布。
    1~10 对10求余数，0~9，加1则为1~10
    2~20 对10求余数，0~9，加1则为1~10
    3~30 对10求余数，0~9，加1则为1~10
    4~40 对10求余数，0~9，加1则为1~10
    因此，要截断41~49 的数
    """
    def rand7(self):
        return int(np.random.uniform(1, 8))

    def rand10(self):
        while True:
            rand_num = (self.rand7() - 1) * 7 + self.rand7()
            if rand_num <= 40:
                return rand_num % 10 + 1


class Solution1:
    """
    给定一个函数rand5()，该函数可以随机生成1~5的整数，且概率相同，现在要求使用该函数生成rand7()，使函数rand7()可以随机等概率生成1~7的概率。
    """
    def rand5(self):
        return int(np.random.uniform(1, 6))

    def rand7(self):
        return ((self.rand5() - 1) * 5 + self.rand5()) % 5 + 1


if __name__ == '__main__':
    S = Solution()
    for i in range(100):
        print(S.rand10())