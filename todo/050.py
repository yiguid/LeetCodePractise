class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = -n

        h = self.myPow(x, n // 2)
        if n % 2 == 0:
            return h * h
        else:
            return h * h * x
