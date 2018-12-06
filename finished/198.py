class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = []
        def tryRob(nums, index):
            if index >= len(nums):
                return 0
            if memo[index] != -1:
                return memo[index]
            res = 0
            for i in range(index, len(nums)):
                res = max(res, nums[i] + tryRob(nums, i + 2))
            memo[index] = res
            return res

        memo = [-1] * len(nums)
        return tryRob(nums, 0)

    def robdp(self, nums):
        n = len(nums)
        dp = [-1] * n
        if n == 0:
            return 0
        #dp[i] means rob nums[0 ... i] max
        dp[0] = nums[0]
        for i in range(1, n):
            for j in range(i + 1):
                if j - 2 >= 0:
                    dp[i] = max(dp[i], nums[j] + dp[j - 2])
                else:
                    dp[i] = max(dp[i], nums[j])
        return dp[n - 1]

    def rob3(self, nums):
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

s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
print(s.robdp([]))
print(s.robdp([1,2,3,1]))
print(s.robdp([2,7,9,3,1]))



