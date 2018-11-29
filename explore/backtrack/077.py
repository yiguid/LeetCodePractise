class Solution:
    res = []
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def comb(n, k, i, c):
            if len(c) == k:
                self.res.append(c[:]) #deep copy
                return
            for j in range(i, n + 1):
                c.append(j)
                comb(n, k, j + 1, c)
                c.pop()
            return

        self.res = []
        if n <= 0 or k <= 0 or k > n:
            return []
        comb(n, k, 1, [])

        return self.res
        


s = Solution()

print(s.combine(4,2))
print(s.combine(4,1))
print(s.combine(1,2))