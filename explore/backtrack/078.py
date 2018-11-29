class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, start, ans):
            res.append(ans[:])
            for i in range(start, len(nums)):
                ans.append(nums[i])
                dfs(nums, i + 1, ans)
                ans.pop()


        res = []
        if len(nums) == 0:
            return [[]]
        dfs(nums, 0, [])
        return res


s = Solution()
print(s.subsets([]))
print(s.subsets([1,2,3]))
print(s.subsets([1,2,3,4]))