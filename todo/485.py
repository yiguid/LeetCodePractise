class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                ret = max(ret, count)
                count = 0
        ret = max(ret, count)
        return ret

        


s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))