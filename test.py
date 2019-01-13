class Solution:
    def swap(self, a, b):
        a, b = b, a

    def swap_array(self, nums):
        nums[0], nums[1] = nums[1], nums[0]
        self.swap(nums[0], nums[1])
        print(nums)


s = Solution()
a = 10
b = 20
s.swap(a, b)
print(a)
print(b)

nums = [1,2]
s.swap_array(nums)
print(nums)

