class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        v0 = -1 #[0,v0] are 0
        v2 = len(nums) #[v2, len(nums) - 1] are 2
        i = 0
        while i < v2:
            if nums[i] == 0:
                nums[v0 + 1], nums[i] = nums[i], nums[v0 + 1]
                v0 += 1
                i += 1
            elif nums[i] == 2:
                nums[v2 - 1], nums[i] = nums[i], nums[v2 - 1]
                v2 -= 1
            else:
                i += 1
        return nums

        

s = Solution()
print(s.sortColors([1,1,2,0]))
print(s.sortColors([2,0,2,1,1,0]))