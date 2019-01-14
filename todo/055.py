class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l == 0:
            return False
        if l == 1:
            return True
        dp = [False] * l
        if nums[0] != 0:
            dp[0] = True
        for i in range(l - 1):
            if not dp[i]:
                continue
            for j in range(nums[i] + 1):
                if i + j < l:
                    dp[i + j] = True
        return dp[l - 1]



s = Solution()
print(s.canJump([1]))
print(s.canJump([0,2,1]))
print(s.canJump([0,1,1]))
print(s.canJump([1,1]))
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))