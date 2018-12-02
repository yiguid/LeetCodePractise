class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def tryRob(nums):
            length = len(nums)
            if length == 0:
                return 0
            if length == 1:
                return nums[0]
            if length == 2:
                return max(nums[:2])
            dp = nums
            if nums[1] < nums[0]:
                dp[1] = dp[0]
            for i in range(2, length):
                dp[i] = max(dp[i] + dp[i-2], dp[i-1])
            return dp[-1]

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        return max(tryRob(nums[0:n-1]), nums[n - 1] + tryRob(nums[1:n - 2]))

s = Solution()
print(s.rob([]))
print(s.rob([2,3,2]))
print(s.rob([1,2,3,1]))