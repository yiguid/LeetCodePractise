class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = [False] * n
        ll = [False] * (2 * n - 1)
        rl = [False] * (2 * n - 1)

        def place(n, row, ans):
            if row == n:
                positions.append(ans[:])
                return
            for i in range(n):
                if not col[i] and not ll[row + i] and not rl[row - i + n - 1]:
                    ans.append(i)
                    col[i] = True
                    ll[row + i] = True
                    rl[row - i + n - 1] = True
                    place(n, row + 1, ans)
                    ans.pop()
                    col[i] = False
                    ll[row + i] = False
                    rl[row - i + n - 1] = False
            return

        positions = []
        place(n, 0, [])

        res = []
        for pos in positions:
            s = []
            for p in pos:
                l = ""
                for i in range(n):
                    if i == p:
                        l += "Q"
                    else:
                        l += "."
                s.append(l)
            res.append(s[:])

        return res



s = Solution()
print(s.solveNQueens(-1))