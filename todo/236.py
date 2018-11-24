# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def inTree(root, node):
            if not node:
                return True
            if node and not root:
                return False
            if node == root:
                return True
            else:
                return inTree(root.left, node) or inTree(root.right, node)

        if root == None:
            return root
        if root == p or root == q:
            return root
        if inTree(p, q):
            return p
        if inTree(q, p):
            return q
        if inTree(root.left, p) and inTree(root.left, q):
            return self.lowestCommonAncestor(root.left, p ,q)
        elif inTree(root.right, p) and inTree(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

