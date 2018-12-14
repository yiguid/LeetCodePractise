class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return l
        i = 1
        while i < l and nums[i] == nums[0]:
            i += 1
        if i == l:
            return 1
        ret = 2
        if nums[i] > nums[0]:
            flag = False
        else:
            flag = True
        val = nums[0]
        for j in range(i, l):
            if flag and nums[j] > val or not flag and nums[j] < val:
                ret += 1
                flag = not flag
            val = nums[j]
        return ret

s = Solution()
print(s.wiggleMaxLength([]))
print(s.wiggleMaxLength([1]))
print(s.wiggleMaxLength([2,2]))
print(s.wiggleMaxLength([2,1]))
print(s.wiggleMaxLength([1,7,4,9,2,5]))
print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
