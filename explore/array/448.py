class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # no extra space
        i = 0
        res = []
        while i < len(nums):
            if nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res
        
    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myset = (len(nums)+1) * [False]
        myset[0] = True
        for num in nums:
            myset[num] = True
        
        # result = []
        # for element,existed in enumerate(myset):
        #     if not existed:
        #         result.append(element)
        # return result
        
        return [element for element,existed in enumerate(myset) if not existed]

s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))