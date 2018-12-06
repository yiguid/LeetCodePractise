class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sumn = sum(nums)
        if sumn < S or (sumn - S) % 2 != 0:
            return 0
        target = (sumn - S) // 2
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for n in nums:
            for i in range(target, -1, -1):
                if i >= n:
                    dp[i] += dp[i - n]
        return dp[-1]
        


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1],3))
