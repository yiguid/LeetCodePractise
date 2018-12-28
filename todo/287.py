class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]
        # return -1
        if len(nums) == 0:
            return -1

        head = slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        while slow != head:
            head = nums[head]
            slow = nums[slow]
        return head


        

s = Solution()
print(s.findDuplicate([]))
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))