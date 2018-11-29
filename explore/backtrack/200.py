class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        d = [[-1,0],[0,1],[1,0],[0,-1]]
        visited = []
        for i in range(m):
            visited.append([False] * n)
        def inGrid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        def dfs(grid, x, y):
            visited[x][y] = True
            for i in range(4):
                newx = x + d[i][0]
                newy = y + d[i][1]
                if inGrid(newx,newy) and not visited[newx][newy] and grid[newx][newy] == 1:
                    dfs(grid, newx, newy)
            return


        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    res += 1
                    dfs(grid, i, j)

        return res

s = Solution()
area1 = [
[1,1,1,1,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,0]
]

area2 = [
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]
]

print(s.numIslands(area1))
print(s.numIslands(area2))



