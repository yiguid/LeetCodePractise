class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l = len(triangle)
        if l <= 0:
            return 0
        if l == 1:
            return triangle[0][0]
        for i in range(1, l):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][i] += triangle[i - 1][i - 1]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

        return min(triangle[l - 1])


s = Solution()
tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

tri2 = [
     [2]
]
print(s.minimumTotal(tri2))