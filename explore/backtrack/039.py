class Solution:
    res = []
    def combinationSum(self, candidates, target):
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
                ans.append(candidates[j])
                comb(candidates, j, target, ans)
                ans.pop()
            return

        self.res = []
        if len(candidates) <= 0 and target != 0:
            return []
        comb(candidates, 0, target, [])

        return self.res
        


s = Solution()

print(s.combinationSum([2,3,6,7],7))
print(s.combinationSum([2,3,5],8))