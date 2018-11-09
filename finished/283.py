class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0 #next arrange position
        #iterate from 0 to last = len(nums) - 1
        for i in range(len(nums)):
        	if nums[i]:
        		temp = nums[i]
        		nums[i] = nums[k]
        		nums[k] = temp
        		k += 1




s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
print(s.moveZeroes([12,0,0,3,12]))