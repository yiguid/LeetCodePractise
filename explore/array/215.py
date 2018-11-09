class Solution:

    def partition(self, nums):
        key = nums[0]
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[j] >= key:
                j -= 1
            while i < j and nums[i] <= key:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[0], nums[i] = nums[i], nums[0]
        return i


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        index = self.partition(nums)
        if index == len(nums) - k:
            return nums[index]
        elif index < len(nums) - k:
            return self.findKthLargest(nums[index + 1:], k)
        else:
            return self.findKthLargest(nums[:index], k - (len(nums) - index))



s = Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6],4))
print(s.findKthLargest([7,6,5,4,3,2,1],5))