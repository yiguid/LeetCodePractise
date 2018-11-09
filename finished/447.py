class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            dic = {}
            for j in range(len(points)):
                if i != j:
                    dis = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                    if dis in dic:
                        dic[dis] += 1
                    else:
                        dic[dis] = 1
            for d in dic:
                res += dic[d] * (dic[d] - 1)
        return res




s = Solution()

print(s.numberOfBoomerangs([[0,0],[1,0],[2,0]]))