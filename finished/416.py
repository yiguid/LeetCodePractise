class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        c = sum(nums)
        if n == 0 or c % 2 != 0:
            return False
        c = c // 2
        dp = [False] * (c + 1)
        for i in range(c + 1):
            if nums[0] == i:
                dp[i] = True
        for i in range(1, n):
            for j in range(c, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[c]



s = Solution()
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 2, 3, 5]))