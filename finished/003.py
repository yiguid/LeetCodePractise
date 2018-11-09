class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,start = 0,0
        m = {}
        for i in range(len(s)):
        	if s[i] in m:
        		start = max(start, m[s[i]] + 1)
        	m[s[i]] = i
        	l = max(l, i - start + 1)

        return l

    def lengthOfLongestSubstring2(self,s):
        f = [0] * 256
        l = 0
        r = -1
        res = 0
        while l < len(s):
            if r + 1 < len(s) and f[ord(s[r + 1])] == 0:
                r += 1
                f[ord(s[r])] += 1
            else:
                f[ord(s[l])] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

s = Solution()
print(s.lengthOfLongestSubstring(' '))
print(s.lengthOfLongestSubstring('abba'))
print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring('bbbb'))
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring2('pwwkek'))
