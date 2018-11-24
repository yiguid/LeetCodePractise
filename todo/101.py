# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(p, q):
            if p == None or q == None:
                return p is q
            return p.val == q.val and isSym(p.left, q.right) and isSym(p.right, q.left)
        return isSym(root,root)