class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s)
        tlen = len(t)
        if tlen < slen or tlen == 0 and slen != 0:
            return False

        si = 0
        ti = 0
        while si < slen and ti < tlen:
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                ti += 1
        if si == slen:
            return True
        else:
            return False


        # solution 2
        # for c in s:
        #     i = t.find(c)
        #     if i == -1:
        #         return False
        #     else:
        #         t = t[i+1:]
        # return True


s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))
print(s.isSubsequence("", "ahbgdc"))
print(s.isSubsequence("abc", ""))