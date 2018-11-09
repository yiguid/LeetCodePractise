class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        unHappy = {}
        while True:
            unHappy[n] = True
            num = 0
            while n > 0:
                num += (n % 10) ** 2
                n //= 10
            if num == 1:
                return True
            elif num in unHappy:
                return False
            else:
                n = num


s = Solution()

print(s.isHappy(19))