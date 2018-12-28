class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = digits[-1] + 1
        ret = []
        if num < 10:
            ret = digits[:-1] + [num]
        else:
            t = num // 10
            ret = [num % 10]
            for i in range(len(digits) - 2, -1, -1):
                ret = [(digits[i] + t) % 10] + ret
                t = (digits[i] + t) // 10
            if t > 0:
                ret = [t] + ret
        return ret
        

s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([4,3,2,9]))
print(s.plusOne([9,9,9,9]))