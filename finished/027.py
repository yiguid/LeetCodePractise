class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        k = 0 #next arrange position
        #iterate from 0 to last = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        return k

        




s = Solution()
print(s.removeElement([3,2,2,3],3))
print(s.removeElement([0,1,2,2,3,0,4,2],2))