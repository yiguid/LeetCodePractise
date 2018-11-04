class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [0]
        ret = []
        for i in range(len(nums) - 1):
            c = 0
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    c += 1
            ret.append(c)
        ret.append(0)
        return ret
        

s = Solution()
print(s.countSmaller([1,8,6,2,5,4,8,3,7]))


print(s.countSmaller([5,2,6,1]))