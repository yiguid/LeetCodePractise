# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        if mid + 1 < len(nums):
            root.right = self.sortedArrayToBST(nums[mid + 1:])
        else:
            root.right = None
        return root



    def printTrees(self, root):
        if root != None:
            self.printTrees(root.left)
            print(root.val)
            self.printTrees(root.right)


s = Solution()

root = s.sortedArrayToBST([-10,-3,0,5,9])

s.printTrees(root)