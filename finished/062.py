class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0
        dp = []
        for i in range(m):
            dp.append([1] * n)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

        # for i in range(m):
        #     print(dp[i])


s = Solution()
print(s.uniquePaths(3,7))