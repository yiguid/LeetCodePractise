class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # for i in range(x // 2 + 1):
        #     if i * i == x:
        #         return i
        #     elif i * i > x:
        #         return i - 1
        #     else:
        #         continue
        # return 1
        if x <= 1:
            return x
        left = 1
        right = x // 2
        while left < right:
            mid = (left + right + 1) // 2
            if x == mid * mid:
                return mid
            elif x > mid * mid:
                left = mid
            else:
                right = mid - 1
        return left
        

s = Solution()

print(s.mySqrt(0))
print(s.mySqrt(1))
print(s.mySqrt(2))
print(s.mySqrt(3))
print(s.mySqrt(4))
print(s.mySqrt(15))
print(s.mySqrt(16))
print(s.mySqrt(17))