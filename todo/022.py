class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        def dfs(left, right, cur):
            if left > right:
                return

            if left == 0 and right == 0:
                ret.append(cur)

            if left:
                dfs(left - 1, right, cur + "(")

            if right:
                dfs(left, right - 1, cur + ")")
        dfs(n, n, "")
        return ret
        

s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
print(s.generateParenthesis(5))