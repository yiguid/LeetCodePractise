class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        k = 0 #next position
        for i in range(1,len(nums)):
        	if nums[i] != nums[k]:
        		k += 1
        		nums[i], nums[k] = nums[k], nums[i]
        return k + 1
        


s = Solution()
print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))