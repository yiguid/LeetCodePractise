class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen = len(s)
        plen = len(p)
        i, j, istar, jstar = 0, 0, -1, -1
        while i < slen:
            if j < plen and p[j] in {s[i], '?'}:
                i += 1
                j += 1
            elif j < plen and p[j] == '*':
                istar = i
                jstar = j + 1
                j += 1
            elif istar != -1 and jstar != -1:
                istar += 1
                i, j = istar, jstar
            else:
                return False

        while j < plen and p[j] == '*':
            j += 1

        return j == plen

s = Solution()
print(s.isMatch("adceb", "*a*b"))
print(s.isMatch("acdcb", "a*c?b"))