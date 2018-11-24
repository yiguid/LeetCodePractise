# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(root, lower_bound, upper_bound):
            if root and root.val <= lower_bound:
                return False
            if root and root.val >= upper_bound:
                return False
            res = True
            if root.left:
                res = res and valid(root.left, lower_bound, root.val)
            if root.right:
                res = res and valid(root.right, root.val, upper_bound)
            return res

        if not root:
            return True
        return valid(root, - 2 ** 32, 2 ** 32) 