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


s = Solution()
print(s.lengthOfLongestSubstring(' '))
print(s.lengthOfLongestSubstring('abba'))
print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring('bbbb'))
print(s.lengthOfLongestSubstring('abcabcbb'))