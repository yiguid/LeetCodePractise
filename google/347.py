from random import randint
import collections
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        p = []
        for key, val in counts.iteritems():
            p.append((-val, key))
        self.kthElement(p, k)
 
        result = []
        for i in range(k):
            result.append(p[i][1])
        return result
 
    def kthElement(self, nums, k):
        def PartitionAroundPivot(left, right, pivot_idx, nums):
            pivot_value = nums[pivot_idx]
            new_pivot_idx = left
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                    new_pivot_idx += 1
 
            nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
            return new_pivot_idx
 
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k - 1:
                return
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1
                left = new_pivot_idx + 1

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))

