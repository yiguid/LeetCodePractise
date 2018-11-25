class Solution:
    res = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def comb(candidates, start, target, ans):
            if sum(ans) == target:
                self.res.append(ans[:]) #deep copy
                return
            if sum(ans) > target:
                return
            for j in range(start, len(candidates)):
                if j > start and candidates[j] == candidates[j - 1]:
                    continue
                ans.append(candidates[j])
                comb(candidates, j + 1, target, ans)
                ans.pop()
            return

        self.res = []
        if len(candidates) <= 0 and target != 0:
            return []
        candidates.sort()
        comb(candidates, 0, target, [])

        return self.res
        


s = Solution()

print(s.combinationSum2([10,1,2,7,6,1,5],8))
print(s.combinationSum2([2,5,2,1,2],5))