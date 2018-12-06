class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        if len(g) == 0 or len(s) == 0:
            return 0
        g.sort(reverse = True)
        s.sort(reverse = True)
        si = 0
        gi = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                count += 1
                si += 1
                gi += 1
            else:
                gi += 1

        return count