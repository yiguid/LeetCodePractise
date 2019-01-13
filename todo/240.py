class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
        return False
        

s = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target = 30

print(s.searchMatrix(matrix, target))