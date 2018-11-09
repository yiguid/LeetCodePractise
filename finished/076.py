class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        right = -1 # [left,right] are the window
        slen = len(s)
        tlen = len(t)

        if not t or not s:
            return ""

        if tlen > slen:
            return ""

        dic = {}
        for c in t:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        dlen = len(dic)
        minlen = slen + 1
        res = ""
        match = 0
        for right in range(slen):
            #move right
            if s[right] in dic:
                dic[s[right]] -= 1
                if dic[s[right]] == 0:
                    match += 1
            while match == dlen and left <= right:
                #output
                if right - left + 1 < minlen:
                    minlen = right - left + 1
                    res = s[left:right + 1]
                #move left
                if s[left] in dic:
                    dic[s[left]] += 1
                    if dic[s[left]] == 1:
                        match -= 1
                left += 1
                
        return res



s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))
print(s.minWindow("a","a"))
print(s.minWindow("abc","b"))
print(s.minWindow("bbaac","aba"))