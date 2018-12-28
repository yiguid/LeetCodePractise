class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            res *= 26
            res += ord(c) - ord('A') + 1
        return res


s = Solution()
print(s.titleToNumber(""))
print(s.titleToNumber("A"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("ZY"))