class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper()
        ret = ""
        dash = 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] == "-":
                continue
            else:
                ret = S[i] + ret
                dash += 1
            if dash == K:
                ret = "-" + ret
                dash = 0
        if len(ret) > 0 and ret[0] == "-":
            ret = ret[1:]
        return ret


s = Solution()
print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(s.licenseKeyFormatting("2-5g-3-J", 2))
print(s.licenseKeyFormatting("---", 2))