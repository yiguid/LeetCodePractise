class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1


    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(numbers):
            if target - num in dict:
                return [dict[target - num] + 1, i + 1]
            else:
                dict[num] = i



s = Solution()
print(s.twoSum([2,7,11,15],9))