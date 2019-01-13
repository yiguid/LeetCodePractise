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
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 13

print(s.searchMatrix(matrix, target))