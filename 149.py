# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            dic = {}
            same = 0
            for j in range(i + 1, len(points)):
                if points[i].y == points[j].y:
                    if points[i].x == points[j].x:
                        same += 1
                        continue
                    else:
                        k = 'i'
                else:
                    k = (points[i].x - points[j].x) / (points[i].y - points[j].y)
                if not k in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1
            mostk = 0
            for key in dic:
                if dic[key] > mostk:
                    mostk = dic[key]
            
            res = max(res, mostk + same + 1)
        return res

s = Solution()

print(s.maxPoints([Point(1,1),Point(2,2),Point(3,3)]))

print(s.maxPoints([Point(1,1),Point(3,2),Point(5,3),Point(4,1),Point(2,3),Point(1,4)]))