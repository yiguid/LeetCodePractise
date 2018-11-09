class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        res = []
        for s in strs:
            hash_s = ''.join(sorted(s))
            if hash_s in group:
                group[hash_s].append(s)
            else:
                group[hash_s] = [s]
        for key in group:
            res.append(group[key])
        return res
        
s = Solution()

print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))