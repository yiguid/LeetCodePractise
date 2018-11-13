class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2:
            return True
        flag = -1
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                if flag == 0:
                    return False
                else:
                    flag = 1
            elif A[i] == A[i + 1]:
                continue
            else:
                if flag == 1:
                    return False
                else:
                    flag = 0
        return True