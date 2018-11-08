import time

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        


s = Solution()
start = time.clock()

print(s.fourSum([1, 0, -1, 0, -2, 2], 0))

print(s.fourSum([0,0,0,0], 0))

end = time.clock()

print(end - start)