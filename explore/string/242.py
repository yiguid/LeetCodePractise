class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return all(s.count(c) == t.count(c) for c in string.ascii_lowercase)