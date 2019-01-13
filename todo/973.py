class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def dis(point):
            return pow(point[0], 2) + pow(point[1], 2)

        def partition(l, r):
            val = dis(points[r])
            p = l
            for i in range(l, r):
                if dis(points[i]) < val:
                    points[i], points[p] = points[p], points[i]
                    p += 1
            points[p], points[r] = points[r], points[p]
            return p 


        def kClosest(l, r, K):
            if 0 < K < r - l + 1:
                p = partition(l, r)
                if p - l + 1 == K:
                    return
                elif p - l + 1 < K:
                    kClosest(p + 1, r, K - (p - l + 1))
                else:
                    kClosest(l, p - 1, K)

        kClosest(0, len(points) - 1, K)
        return points[:K]

s = Solution()
print(s.kClosest([[1,3],[-2,2]], 1))
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))