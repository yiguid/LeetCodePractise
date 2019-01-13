class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] > 0 and nums[i] - 1 < l and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                t = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[t - 1] = t
            else:
                i += 1

        for i in range(l):
            if nums[i] != i + 1:
                return i + 1
        return l + 1

s = Solution()
print(s.firstMissingPositive([1,2,0]))
print(s.firstMissingPositive([3,4,-1,1]))
print(s.firstMissingPositive([7,8,9,11,12]))