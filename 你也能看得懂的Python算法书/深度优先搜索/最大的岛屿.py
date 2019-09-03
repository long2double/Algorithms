class Solution:
    def maxAreaOfIsIand(self, grid):
        def fill(x, y, current):
            if x < 0 or x > n - 1 or y < 0 or y > m - 1 or grid[x][y] != '1':
                return
            else:
                queue.append((x, y))
                grid[x][y] = '2'
                current += 1
                return max(maxArea, current)

        def dfs(x, y, current):
            fill(x, y, current)

            while queue:
                cur = queue.pop(0)
                i = cur[0]
                j = cur[1]
                fill(i + 1, j)
                fill(i - 1, j)
                fill(i, j + 1)
                fill(i, j - 1)


        row = len(grid)
        col = len(grid[0])

        queue = []
        maxArea = 0
        for n in range(row):
            for m in range(col):
                current = 0
                dfs(n, m, current)


