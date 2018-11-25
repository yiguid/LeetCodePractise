# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        if not root.left and not root.right and sum == root.val:
            res.append([root.val])
            return res
        if root.left:
            path = self.pathSum(root.left, sum - root.val)
            for p in path:
                res.append([root.val] + p)
        if root.right:
            path = self.pathSum(root.right, sum - root.val)
            for p in path:
                res.append([root.val] + p)

        return res