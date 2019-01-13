from random import randint
class Solution:
    def partition(self, nums, left, right, rp):
        val = nums[rp]
        p = left
        nums[rp], nums[right] = nums[right], nums[rp]
        for i in range(left, right):
            if nums[i] < val:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        nums[right], nums[p] = nums[p], nums[right]
        return p

    def quick_sort(self, nums, left, right):
        if left < right:
            rp = randint(left, right)
            p = self.partition(nums, left, right, rp)
            self.quick_sort(nums, 0, p - 1)
            self.quick_sort(nums, p + 1, right)

    def quick(self, nums):
        l = len(nums)
        if l <= 1:
            return nums
        self.quick_sort(nums, 0, l - 1)


s = Solution()
nums = [1,0,9,5,3,23,2,5,7,8,96,4,3,3,2,3,1,2,4,5,5,6]
s.quick(nums)
print(nums)