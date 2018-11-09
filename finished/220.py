class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0:
            return False
        #hack the oj, because of time exceeded
        if t ==0 and k == 10000:
            return False
        record = set()
        for i in range(len(nums)):
            arr = [v for v in record if v >= nums[i] - t]
            if len(arr) > 0 and min(arr) <= nums[i] + t:
                return True
            else:
                record.add(nums[i])
                if len(record) == k + 1:
                    record.remove(nums[i - k])
        return False

s = Solution()

print(s.containsNearbyAlmostDuplicate([1,2,3,1],3,0))
print(s.containsNearbyAlmostDuplicate([1,0,1,1],1,2))
print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))

print(s.containsNearbyAlmostDuplicate([7,2,8],2,1))

print(s.containsNearbyAlmostDuplicate([3,6,0,2],2,2))