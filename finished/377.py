class Solution:

    ans = 0
    def combinationSum4dfs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dfs(target):
            if target == 0:
                self.ans += 1
            for i in range(len(nums)):
                if nums[i] <= target:
                    dfs(target - nums[i])
        nums.sort()
        self.ans = 0
        dfs(target)
        return self.ans

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [1]
        i = 1
        while i <= target:
            count = 0
            for n in nums:
                if n > i:
                    break
                count += dp[i - n]
            dp.append(count)
            i += 1
        return dp[target]
        


s = Solution()
print(s.combinationSum4([1, 2, 3], 4))