class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def perm(i):
            if i == len(nums) - 1:
                res.append(nums[:])
                return
            used = set()
            for j in range(i, len(nums)):
                if nums[j] not in used:
                    used.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    perm(i + 1)
                    nums[i], nums[j] = nums[j], nums[i]
        
        res = []
        nums.sort()
        perm(0)
        return res
        

s = Solution()
print(s.permuteUnique([1,1,2]))
print(s.permuteUnique([1]))
print(s.permuteUnique([1,2,3]))