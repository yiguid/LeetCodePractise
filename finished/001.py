class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
        	for j in range(i + 1,len(nums)):
        		if nums[i] + nums[j] == target:
        			return [i,j]
        return []

    def twoSum2(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []


s = Solution()
print(s.twoSum([2,7,11,15],9))
print(s.twoSum2([2,7,11,15],9))
