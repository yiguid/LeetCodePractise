import heapq

class Solution:
    def heapsort(self, iterable):
        heap = []
        for value in iterable:
            heapq.heappush(heap,value) #[0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
        return [heapq.heappop(heap) for i in range(len(heap))]

s = Solution()
print(s.heapsort([1,3,5,7,9,2,4,6,8,0]))