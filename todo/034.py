class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(nums, target):
            l = 0
            h = len(nums)
            while l < h:
                m = l + (h - l) // 2
                if nums[m] >= target:
                    h = m
                else:
                    l = m + 1
            return l


        l = len(nums)
        if l < 1 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        first = binarySearch(nums, target)
        last = binarySearch(nums, target + 1) - 1
        if nums[first] != target or nums[last] != target:
            return [-1, -1]
        else:
            return [first, last]


s = Solution()
print(s.searchRange([], 1))
print(s.searchRange([1], 1))
print(s.searchRange([8,8], 8))
print(s.searchRange([5,7,8,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))