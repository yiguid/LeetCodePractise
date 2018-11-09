class Solution:

    def partition(self, nums, left, right):
        key = nums[left]
        i = left
        j = right
        while i < j:
            while i < j and nums[j] >= key:
                j -= 1
            while i < j and nums[i] <= key:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[i] = nums[i], nums[left]
        return i


    def quick(self, nums, left, right):
        if(left < right):
            index = self.partition(nums, left, right)
            self.quick(nums, index + 1, right)
            self.quick(nums, left, index - 1)


s = Solution()

nums1 = [3,2,1,5,6,4]
s.quick(nums1,0,len(nums1) - 1)
print(nums1)

nums2 = [3,2,3,1,2,4,5,5,6]
s.quick(nums2,0,len(nums2) - 1)
print(nums2)

nums3 = [7,6,5,4,3,2,1]
s.quick(nums3,0,len(nums3) - 1)
print(nums3)

