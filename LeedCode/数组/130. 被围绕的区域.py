"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X

解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填
充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""


class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        def fill(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != 'O':
                return
            else:
                queue.append((x, y))
                board[x][y] = '#'  # 作用一：标记已经走过了，作用二：最后遍历的时候，扣除边界

        def bfs(x, y):
            fill(x, y)

            while queue:  # 判断边界是否连通
                cur = queue.pop(0)
                i = cur[0]
                j = cur[1]
                fill(i + 1, j)
                fill(i - 1, j)
                fill(i, j + 1)
                fill(i, j - 1)

        if len(board) == 0:
            return

        m = len(board)  # 行
        n = len(board[0])  # 列
        queue = []
        for i in range(n):  # 第一行和最后一行
            bfs(0, i)
            bfs(m - 1, i)

        for j in range(1, m - 1):  # 第一列和最后一列
            bfs(j, 0)
            bfs(j, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

