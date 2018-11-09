class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left = 0
        right = -1 #[left,right] = p[:]
        plen = len(p)
        slen = len(s)
        table = {} #store the appearance
        match = 0 #matched p numbers
        res = []

        #init
        for c in p:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        stable = len(table)

        while right < slen and left < slen - plen + 1:
            #if right + 1 has and not plen
            if right + 1 < slen and right - left + 1 < plen:
                if s[right + 1] in table:
                    table[s[right + 1]] -= 1
                    if table[s[right + 1]] == 0:
                        match += 1
                right += 1
            else:
                if s[left] in table:
                    table[s[left]] += 1
                    if table[s[left]] == 1:
                        match -= 1
                left += 1

            if match == stable:
                res.append(left)
        return res

s = Solution()
print(s.findAnagrams("baa","aa"))
# print(s.findAnagrams("cbaebabacd","abc"))
# print(s.findAnagrams("abab","ab"))