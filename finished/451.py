class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        items = [[v[1], v[0]] for v in dic.items()]
        items.sort(reverse=True)
        res = ''
        for v in items:
            res += v[1]*v[0]
        return res
        

s = Solution()

print(s.frequencySort("tree"))
print(s.frequencySort("cccaaa"))
print(s.frequencySort("Aabb"))