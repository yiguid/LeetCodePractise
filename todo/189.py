class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

s = Solution()
arr = [1,2,3,4,5,6,7]
s.rotate(arr, 3)
print(arr)
