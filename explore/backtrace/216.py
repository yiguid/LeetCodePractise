class Solution:
    res = []
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def comb(n, k, i, c):
            if len(c) == k and sum(c) == n:
                self.res.append(c[:]) #deep copy
                return
            for j in range(i, 10):
                c.append(j)
                comb(n, k, j + 1, c)
                c.pop()
            return

        self.res = []
        if n <= 0 or k <= 0 or n > 45:
            return []
        comb(n, k, 1, [])

        return self.res

s = Solution()

print(s.combinationSum3(3,7))
print(s.combinationSum3(3,9))
print(s.combinationSum3(1,9))