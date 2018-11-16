class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = {}
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
        return sorted(m, key = m.get, reverse = True)[:k]


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))