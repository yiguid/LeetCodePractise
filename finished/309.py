class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        s0 = 0
        s1 = - prices[0]
        s2 = - 2 ** 32
        for i in range(1, len(prices)):
            s0, s1, s2 = max(s0, s2), max(s0 - prices[i], s1), s1 + prices[i]

        return max(s0, s2)

s = Solution()
print(s.maxProfit([1,2,3,0,2]))