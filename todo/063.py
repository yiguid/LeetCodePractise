class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) <= 0 or len(obstacleGrid[0]) <= 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []
        for i in range(m):
            dp.append([0] * n)

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[m - 1][n - 1]

        # for i in range(m):
        #     print(dp[i])


s = Solution()
grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

grid2 = [
  [0,0,0,0],
  [0,1,0,0],
  [0,0,0,0]
]

print(s.uniquePathsWithObstacles(grid2))