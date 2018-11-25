# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        cur = 0
        if not root:
            return None
        node = root
        while node or stack != []:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            cur += 1
            if cur == k:
                return node.val
            node = node.right
        return None