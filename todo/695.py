class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 1

        def dfs(i, j):
            grid[i][j] = count
            area = 1
            if i - 1 >= 0:
                if grid[i - 1][j] == 1:
                    area += dfs(i - 1, j)
            if j - 1 >= 0:
                if grid[i][j - 1] == 1:
                    area += dfs(i, j - 1)
            if i + 1 < m:
                if grid[i + 1][j] == 1:
                    area += dfs(i + 1, j)
            if j + 1 < n:
                if grid[i][j + 1] == 1:
                    area += dfs(i, j + 1)
            return area

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    ret = max(ret, dfs(i,j))
        return ret

s = Solution()
grid = [
[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

grid2 = [[0,0,0,0,0,0,0,0]]
print(s.maxAreaOfIsland(grid))
print(s.maxAreaOfIsland(grid2))

