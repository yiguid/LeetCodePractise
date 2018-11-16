class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        h = [1] * n
        h[0] = h[1] = 0
        for i in range(2, n // 2 + 1):
            if h[i] == 1:
                for j in range(2, n // i + 1):
                    if i * j < n:
                        h[i * j] = 0
        return sum(h)


s = Solution()
print(s.countPrimes(10))