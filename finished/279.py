class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        dp = [n] * (n + 1)
        i = 0
        #init
        while i * i <= n:
            dp[i * i] = 1
            i += 1
        for i in range(1, n):
            j = 1
            while i + j * j <= n:
                t = i + j * j
                dp[t] = min(dp[i] + 1, dp[t])
                j += 1
        return dp[n]


s = Solution()
print(s.numSquares(19))
