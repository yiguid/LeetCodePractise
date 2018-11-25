class Solution:
    res = []
    used = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.used = [False] * len(nums)
        def perm(nums, ans):
            if len(ans) == len(nums):
                self.res.append(ans[:])
                return
            for i in range(len(nums)):
                if not self.used[i]:
                    ans.append(nums[i])
                    self.used[i] = True
                    perm(nums, ans)
                    ans.pop()
                    self.used[i] = False
            return

        self.res = []
        if len(nums) <= 0:
            return [] 
        perm(nums, [])
        return self.res
        

s = Solution()
print(s.permute([]))
print(s.permute([1]))
print(s.permute([1,2,3]))