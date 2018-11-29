class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        m = len(board)
        n = len(board[0])
        visited = []
        for i in range(m):
            visited.append([False] * n)
        d = [[-1,0],[0,1],[1,0],[0,-1]]

        def inBoard(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        def dfs(board, x, y):
            if board[x][y] == "O" and not visited[x][y]:
                visited[x][y] = True
                for i in range(4):
                    newx = x + d[i][0]
                    newy = y + d[i][1]
                    if inBoard(newx, newy) and not visited[newx][newy]:
                        dfs(board, newx, newy)    
            return

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    dfs(board, i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"

        


s = Solution()
board = [
["X","X","X","X"],
["X","O","O","X"],
["X","X","O","O"],
["X","O","X","X"],
["X","O","X","X"]
]

s.solve(board)
for row in board:
    print(row)