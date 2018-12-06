class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return res
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    #count edge
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        res += 1
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        res += 1
                    if i + 1 == m or grid[i + 1][j] == 0:
                        res += 1
                    if j + 1 == n or grid[i][j + 1] == 0:
                        res += 1
        return res

s = Solution()
grid = [[1,1,1,1],
 [1,1,1,1],
 [1,1,1,1],
 [1,1,1,1]]
print(s.islandPerimeter(grid))