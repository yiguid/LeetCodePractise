class Solution:
    def updateMatrix1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        ret = [[10000] * n for i in range(m)]
        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        def dfs(matrix, i, j, val):
            if i >= 0 and i < m and j >= 0 and j < n and ret[i][j] > val:
                ret[i][j] = val
                for d in range(4):
                    dfs(matrix, i + direction[d][0], j + direction[d][1], val + 1)
            else:
                return

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    continue
                else:
                    dfs(matrix, i, j, 0)

        return ret

    def updateMatrix(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        ret = [[10000] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ret[i][j] = 0
                else:
                    if i > 0:
                        ret[i][j] = min(ret[i][j], ret[i - 1][j] + 1)
                    if j > 0:
                        ret[i][j] = min(ret[i][j], ret[i][j - 1] + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i < m - 1:
                        ret[i][j] = min(ret[i][j], ret[i + 1][j] + 1)
                    if j < n - 1:
                        ret[i][j] = min(ret[i][j], ret[i][j + 1] + 1)

        return ret


s = Solution()
matrix = [
[0,0,0],
[0,1,0],
[0,0,0]
]

matrix2 = [
[0,0,0],
[0,1,0],
[1,1,1]
]

matrix3 = [
[0,1,1],
[1,1,1],
[1,1,0]
]

matrix4 = [
[0,1,0,1],
[1,0,1,1],
[1,1,1,1],
[0,1,1,0]
]

print(s.updateMatrix(matrix))
print(s.updateMatrix(matrix2))
print(s.updateMatrix(matrix3))
print(s.updateMatrix(matrix4))


