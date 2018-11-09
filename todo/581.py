class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r - 1 and nums[r - 1] < nums[r]:
            r -= 1
        while l + 1 < r and nums[l + 1] > nums[l]:
            l += 1
        return r - l + 1
        #todo more 
        return len(nums)

        

s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(s.findUnsortedSubarray([1,2,3]))