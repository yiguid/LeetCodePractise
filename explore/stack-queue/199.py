# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        queue = []
        queue.append([0, root])
        while len(queue) != 0:
            q = queue.pop(0)
            if len(res) < q[0] + 1:
                res.append(q[1].val)
            if q[1].right != None:
                queue.append([q[0] + 1, q[1].right])
            if q[1].left != None:
                queue.append([q[0] + 1, q[1].left])
        return res