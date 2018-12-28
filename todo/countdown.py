class Solution:
  def cal(self, nums, target):
    ans = []
    def dfs(nums, target, exp):
      if len(ans) > 40:
        return
      if len(nums) == 1:
        if nums[0] == target:
          ans.append(exp[0])
          return 
        else:
          return 
      else:
        for i in range(len(nums) - 1):
          for j in range(i + 1, len(nums)):
            v1 = nums[i]
            v2 = nums[j]
            exp1 = exp[i]
            exp2 = exp[j]
            newN = []
            newE = []
            for k in range(6):
              newN[:] = nums[:i] + nums[i + 1:]
              newE[:] = exp[:i] + exp[i + 1:]
              if k == 0:
                newN[j - 1] = v1 + v2
                newE[j - 1] = '(' + exp1 + ' + ' + exp2 + ')'
                dfs(newN, target, newE)
              if k == 1:
                newN[j - 1] = v1 * v2
                newE[j - 1] = '(' + exp1 + ' * ' + exp2 + ')'
                dfs(newN, target, newE)
              if k == 2:
                newN[j - 1] = v1 - v2
                newE[j - 1] = '(' + exp1 + ' - ' + exp2 + ')'
                dfs(newN, target, newE)
              if k == 3:
                newN[j - 1] = v2 - v1
                newE[j - 1] = '(' + exp2 + ' - ' + exp1 + ')'
                dfs(newN, target, newE)
              if k == 4 and v2 != 0:
                newN[j - 1] = v1 // v2
                newE[j - 1] = '(' + exp1 + ' / ' + exp2 + ')'
                dfs(newN, target, newE)
              if k == 5 and v1 != 0:
                newN[j - 1] = v2 // v1
                newE[j - 1] = '(' + exp2 + ' / ' + exp1 + ')'
                dfs(newN, target, newE)
    
    exp = []
    for i in nums:
      exp.append(str(i))
    dfs(nums, target, exp) 
    return ans


s = Solution()
ans = s.cal([75, 50, 2, 3, 8, 7], 812)
for a in ans:
  print(a + " = 812")