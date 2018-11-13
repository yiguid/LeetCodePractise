class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        res = len(nums)
        if nums[0] > nums[-1]:
            return res
        while 0 <= r - 1 and nums[r - 1] <= nums[r]:
            r -= 1
        if r == 0:
            return 0
        while l + 1 <= res - 1 and nums[l + 1] >= nums[l]:
            l += 1
        # process middle part
        b,s = max(nums[l:(r+1)]), min(nums[l:(r+1)])
        while l >= 0 and nums[l] > s:
            l -= 1
        while r <= res - 1 and nums[r] < b:
            r += 1

        return r - l - 1

        

s = Solution()

print(s.findUnsortedSubarray([1,2,3,3,3]))
print(s.findUnsortedSubarray([10,11,12,6,7,8,0,1,2,3]))
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(s.findUnsortedSubarray([1,2,3]))