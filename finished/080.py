class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        k = 0 #position
        t = 0 #times
        cur = 0 #current number position
        for i in range(len(nums)):
            if nums[cur] == nums[i]:
                t += 1
                if i != k:
                    nums[k], nums[i] = nums[i], nums[k]
                if t <= 2:
                    k += 1
            else:
                t = 1
                nums[k], nums[i] = nums[i], nums[k]
                cur = k
                k += 1
        return k

    def removeDuplicates2(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i




s = Solution()
print(s.removeDuplicates2([1]))
print(s.removeDuplicates2([1,1,1,2,2,3]))
print(s.removeDuplicates2([1,1,1,2,2,3]))
print(s.removeDuplicates2([0,0,1,1,1,1,2,3,3]))
