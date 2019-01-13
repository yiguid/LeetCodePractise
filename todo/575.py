class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        l = len(candies)
        s = set()
        for n in candies:
            if not n in s:
                s.add(n)
            if len(s) >= l // 2:
                return l // 2
        return len(s)


s = Solution()
print(s.distributeCandies([0,1]))
print(s.distributeCandies([1,1,2,2,3,3]))
print(s.distributeCandies([1,1,2,3]))