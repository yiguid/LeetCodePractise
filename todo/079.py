class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        d = [[-1,0],[0,1],[1,0],[0,-1]]

        if len(board) == 0 or len(board[0]) == 0:
            return False
        m = len(board)
        n = len(board[0])

        def search(board, word, cur, x, y):
            if cur == len(word) - 1 and board[x][y] == word[cur]:
                return True
            if board[x][y] == word[cur]:
                visited[x][y] = True
                #four direction
                for i in range(4):
                    newx = x + d[i][0]
                    newy = y + d[i][1]
                    if newx >= 0 and newx < m and newy >=0 and newy < n and visited[newx][newy] == False and search(board, word, cur + 1, newx, newy):
                        return True
                visited[x][y] = False
            return False

        visited = []
        for i in range(m):
            visited.append([False] * n)
        for i in range(m):
            for j in range(n):
                if search(board, word, 0, i, j):
                    return True
        return False
        

s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(s.exist(board, "ABCCED"))
print(s.exist(board, "SEE"))
print(s.exist(board, "ABCB"))