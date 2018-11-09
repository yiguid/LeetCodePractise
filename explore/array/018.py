import time

class Solution:
    def twoSum(self, nums, target, prev, results):
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                results.append(prev + [nums[i], nums[j]])
                i += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                j -= 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

    def nSum(self, nums, target, n, prev, results):
        if len(nums) < n or n < 2 or target < nums[0] * n or target > nums[-1] * n:
            results = []
        if n == 2:
            self.twoSum(nums, target, prev, results)
        else:
            for i in range(len(nums) - n + 1):
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    self.nSum(nums[i + 1:], target - nums[i], n - 1, prev + [nums[i]], results)


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        self.nSum(nums, target, 4, [], results)
        return results


s = Solution()
start = time.clock()

print(s.fourSum([1, 0, -1, 0, -2, 2], 0))

print(s.fourSum([0,0,0,0], 0))

end = time.clock()

print(end - start)