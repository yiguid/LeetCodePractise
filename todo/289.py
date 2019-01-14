class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        direction = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live = 0
                for d in direction:
                    x = i + d[0]
                    y = j + d[1]
                    if x >= 0 and x < m and y >= 0 and y < n:
                        if abs(board[x][y]) == 1:
                            live += 1
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
        

s = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

s.gameOfLife(board)
print(board)