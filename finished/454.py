class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        for c in C:
            for d in D:
                if c + d in dic:
                    dic[c + d] += 1
                else:
                    dic[c + d] = 1

        for a in A:
            for b in B:
                if - a - b in dic:
                    res += dic[- a - b]
        return res

s = Solution()
print(s.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))