class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        if x > y:
            x, y = y, x
        while y != 0:
            if x % 2 != y % 2:
                res += 1
            x //= 2
            y //= 2
        return res

s = Solution()
print(s.hammingDistance(1,4))