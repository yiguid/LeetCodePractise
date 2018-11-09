class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        if len(s) != len(t):
            return False
        for i, p in enumerate(s):
            if p in dic:
                if dic[p] != t[i]:
                    return False
            else:
                if not t[i] in dic.values():
                    dic[p] = t[i]
                else:
                    return False
        return True


s = Solution()

print(s.isIsomorphic("egg","add"))
print(s.isIsomorphic("foo","bar"))
print(s.isIsomorphic("paper","title"))