class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        p = []
        for i in range(m):
            p.append([0] * n)
        a = []
        for i in range(m):
            a.append([0] * n)
        d = [[-1,0],[0,1],[1,0],[0,-1]]

        def inMatrix(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        def dfs(matrix, x, y, ocean):
            if ocean[x][y] == 0:
                ocean[x][y] = 1
            for i in range(4):
                newx = x + d[i][0]
                newy = y + d[i][1]
                if inMatrix(newx, newy) and matrix[newx][newy] >= matrix[x][y]:
                    if ocean[newx][newy] == 0:
                        dfs(matrix, newx, newy, ocean)    
            return

        for i in range(m):
            dfs(matrix, i, 0, p)
        for j in range(n):
            dfs(matrix, 0, j, p)

        for j in range(n):
            dfs(matrix, m - 1, j, a)
        for i in range(m):
            dfs(matrix, i, n - 1, a)

        res = []
        for i in range(m):
            for j in range(n):
                if a[i][j] == 1 and p[i][j] == 1:
                    res.append([i, j])
        return res


s = Solution()
matrix = [
[1,2,2,3,5],
[3,2,3,4,4],
[2,4,5,3,1],
[6,7,1,4,5],
[5,1,1,2,4]]

print(s.pacificAtlantic(matrix))

print(s.pacificAtlantic([[1,2,3],[8,9,4],[7,6,5]]))



