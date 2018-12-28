class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        top, right, bottom, left = 0, n, m, 0
        ret = []
        while True:
            for i in range(left, right):
                ret.append(matrix[top][i])
            top += 1
            if top >= bottom:
                break

            for i in range(top, bottom):
                ret.append(matrix[i][right - 1])
            right -= 1
            if left >= right:
                break

            for i in range(right - 1, left - 1, -1):
                ret.append(matrix[bottom - 1][i])
            bottom -= 1
            if top >= bottom:
                break

            for i in range(bottom - 1, top - 1, -1):
                ret.append(matrix[i][left])
            left += 1
            if left >= right:
                break
        return ret


s = Solution()
print(s.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))

print(s.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))