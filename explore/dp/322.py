class Solution:
    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        c = amount
        n = len(coins)
        if n == 0:
            return -1
        if c == 0:
            return 0
        coins.sort()
        maxn = c // coins[0] + 1
        dp = [maxn] * (c + 1)
        for i in range(c + 1):
            if i % coins[0] == 0:
                dp[i] = i // coins[0]

        for i in range(1, n):
            for j in range(c, 0, -1):
                for k in range(j // coins[i] + 1):
                    dp[j] = min(dp[j], dp[j - k * coins[i]] + k)

        if dp[c] == maxn:
            return -1
        else:
            return dp[c]
        # too long time
        
    res = 2 ** 32
    def coinChange(self, coins, amount):
        def dfs(index, amount, count):
            if amount == 0:
                self.res = min(self.res, count)
            for i in range(index, len(coins)):
                if coins[i] <= amount and amount < coins[i] * (self.res - count):
                    dfs(i, amount - coins[i], count + 1)
        coins.sort(reverse = True)
        self.res = 2 ** 32
        dfs(0, amount, 0)
        if self.res < 2 ** 32:
            return self.res
        else:
            return -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))
print(s.coinChange([2, 5, 10, 1], 27))
print(s.coinChange([186,419,83,408], 6249))
print(s.coinChange([3,7,405,436], 8839))
