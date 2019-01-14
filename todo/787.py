import collections
import heapq
class Solution:

    def findCheapestPrice2(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        def findRoute(flights, src, dst, K, cost, visited, best):
            if src == dst:
                return cost
            if K == -1:
                return 1000000
            if cost > best[0]:
                return 1000000
            res = 1000000
            for f in flights:
                if f[0] == src and not f[1] in visited:
                    # print(f[0], f[1], f[2])
                    visited.add(f[1])
                    res = min(res, findRoute(flights, f[1], dst, K - 1, cost + f[2], visited, best))
                    visited.remove(f[1])
            if res == 1000000:
                return 1000000
            else:
                best[0] = res
                return res
        res = findRoute(flights, src, dst, K, 0, set(), [1000000])
        if res == 1000000:
            return -1
        else:
            return res 

    def findCheapestPrice3(self, n, flights, src, dst, K):
        ans = []
        for i in range(n):
            ans.append([1000000] * (K + 1))
        ans[src][0] = 0
        for f in flights:
            if f[0] == src:
                ans[f[1]][0] = f[2]
        for j in range(1, K + 1):
            for i in range(n):
                ans[i][j] = ans[i][j - 1]
            for f in flights:
                ans[f[1]][j] = min(ans[f[1]][j], ans[f[0]][j - 1] + f[2])

        if ans[dst][K] == 1000000:
            return -1
        else:
            return ans[dst][K]

    def findCheapestPrice(self, n, flights, src, dst, K):
        f = collections.defaultdict(dict)
        for a,b,c in flights:
            f[a][b] = c
        dist = {i:1e8 for i in range(n)}
        dist[src] = 0.0
        heap = [(0, src, K + 1)] #cost 0, from src, have k + 1 steps
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    if p + f[i][j] < dist[j]:
                        dist[j] = p + f[i][j]
                        heapq.heappush(heap,(p + f[i][j], j, k - 1))
        return -1
        

s = Solution()
print(s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
print(s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
print(s.findCheapestPrice(5,[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]],0,4,1))
print(s.findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1))
print(s.findCheapestPrice(17,[[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]],13,4,13))