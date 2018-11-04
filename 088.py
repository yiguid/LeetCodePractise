class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #from the last to the first element
        #m - 1 is the last of nums1, n - 1 is the last of nums2, m + n - 1 is the last of ret nums
        while m > 0 and n > 0:
        	if nums1[m - 1] >= nums2[n - 1]:
        		nums1[m + n - 1] = nums1[m - 1]
        		m -= 1
        	else:
        		nums1[m + n - 1] = nums2[n - 1]
        		n -= 1
        while m == 0 and n > 0:
        	nums1[n - 1] = nums2[n - 1]
        	n -= 1

        return nums1


s = Solution()
print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))