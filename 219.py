class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = set()
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            else:
                record.add(nums[i])
                if len(record) == k + 1:
                    record.remove(nums[i - k])
        return False


s = Solution()

print(s.containsNearbyDuplicate([1,2,3,1],3))
print(s.containsNearbyDuplicate([1,0,1,1],1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))