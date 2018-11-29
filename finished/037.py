class Solution:
    flag = False
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = []
        col = []
        cell = []
        for i in range(9):
            row.append([False] * 9)
            col.append([False] * 9)
            cell.append([False] * 9)
        div = [
        [0,0,0,1,1,1,2,2,2],
        [0,0,0,1,1,1,2,2,2],
        [0,0,0,1,1,1,2,2,2],
        [3,3,3,4,4,4,5,5,5],
        [3,3,3,4,4,4,5,5,5],
        [3,3,3,4,4,4,5,5,5],
        [6,6,6,7,7,7,8,8,8],
        [6,6,6,7,7,7,8,8,8],
        [6,6,6,7,7,7,8,8,8]]

        def dfs(board, i, j):
            if i == 9:
                self.flag = True
                return 
            elif j == 8:
                nexti = i + 1
                nextj = 0
            else:
                nexti = i
                nextj = j + 1
            if self.flag:
                return
            if board[i][j] != ".":
                dfs(board, nexti, nextj)
            else:
                for v in range(9):
                    if not row[i][v] and not col[j][v] and not cell[div[i][j]][v]:
                        board[i][j] = str(v + 1)
                        row[i][v] = True
                        col[j][v] = True
                        cell[div[i][j]][v] = True
                        dfs(board, nexti, nextj)
                        if self.flag:
                            return
                        board[i][j] = "."
                        row[i][v] = False
                        col[j][v] = False
                        cell[div[i][j]][v] = False
            return

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num) - 1
                    row[i][num] = True
                    col[j][num] = True
                    cell[div[i][j]][num] = True

        dfs(board, 0, 0)
        
s = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)

for b in board:
    print(b)