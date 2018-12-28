class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            count = 0
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            ret.append(count)
        return ret
        

s = Solution()
print(s.countSmaller([5, 2, 6, 1]))