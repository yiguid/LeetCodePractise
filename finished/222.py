# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        p = q = root
        height = 0 
        while q:
            p = p.left
            q = q.right
            height += 1
        if not p:
            return 2 ** height - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1