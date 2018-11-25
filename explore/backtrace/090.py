class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, start, ans):
            res.append(ans[:])
            for i in range(start, len(nums)):
                if i > start and nums[i - 1] == nums[i]:
                    continue
                ans.append(nums[i])
                dfs(nums, i + 1, ans)
                ans.pop()


        res = []
        if len(nums) == 0:
            return [[]]
        nums.sort()
        dfs(nums, 0, [])
        return res


s = Solution()
print(s.subsetsWithDup([1,2,2]))
print(s.subsetsWithDup([]))
print(s.subsetsWithDup([1,2,3]))