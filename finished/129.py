# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, sum):
            if not root:
                return 0
            if not root.left and not root.right:
                return sum * 10 + root.val
            else:
                return dfs(root.left, sum * 10 + root.val) + dfs(root.right, sum * 10 + root.val)
        return dfs(root, 0)
