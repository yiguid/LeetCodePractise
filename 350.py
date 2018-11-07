class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        res = []
        for n in nums1:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1

        for n in nums2:
            if n in dic and dic[n] > 0:
                dic[n] -= 1
                res.append(n)

        return res



s = Solution()

print(s.intersect([1,2,2,1],[2,2]))
print(s.intersect([4,9,5],[9,4,9,8,4]))