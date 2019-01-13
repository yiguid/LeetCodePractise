class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        if l < 3:
            return 0
        A.sort()
        while l > 2:
            if A[l - 1] < A[l - 2] + A[l - 3]:
                return A[l - 1] + A[l - 2] + A[l - 3]
            else:
                l -= 1
        return 0

s = Solution()
print(s.largestPerimeter([2,1,2]))
print(s.largestPerimeter([1,2,1]))
print(s.largestPerimeter([3,2,3,4]))
print(s.largestPerimeter([3,6,2,3]))