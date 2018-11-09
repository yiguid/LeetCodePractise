import time

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        if len(nums) <= 3:
            return sum(nums)

        closest = sum(nums[:3])
        distance = float("inf")

        for k in range(len(nums) - 1):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                elif s < target:
                    i += 1
                    if abs(s - target) < distance:
                        closest = s
                        distance = abs(s - target)
                else:
                    j -= 1
                    if abs(s - target) < distance:
                        closest = s
                        distance = abs(s - target)
 
        return closest


s = Solution()
start = time.clock()

# print(s.threeSumClosest([-1, 2, 1, -4], 1))
#
# print(s.threeSumClosest([1, 0, -1, 0, -2, 2], 0))
#
# print(s.threeSumClosest([0,0,0,0], 0))

print(s.threeSumClosest([1,1,1,1], 1))

print(s.threeSumClosest([1,1,1,1], -100))

end = time.clock()

print(end - start)