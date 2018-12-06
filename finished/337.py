# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # flag = True means rob the root, else not. return max rob value within this root
        # time limit exceeded
        def tryRob(root, flag):
            if not root:
                return 0
            if not flag:
                return max(tryRob(root.left, True),tryRob(root.left, False)) + max(tryRob(root.right, True),tryRob(root.right, False))
            else:
                res = root.val
                if root.left:
                    res += tryRob(root.left, False)
                if root.right:
                    res += tryRob(root.right, False)
                return res

        return max(tryRob(root, True), tryRob(root, False))

    def rob2(self, root):
        def robBool(root):
            if not root:
                return 0, 0
            robTrueLeft, robFalseLeft = robBool(root.left)
            robTrueRight, robFalseRight = robBool(root.right)
            valueTrue = robFalseLeft + robFalseRight + root.val
            valueFalse = max(robTrueLeft, robFalseLeft) + max(robTrueRight, robFalseRight)
            return valueTrue, valueFalse

        robTrue, robFalse = robBool(root)
        return max(robTrue, robFalse)

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(1)

s = Solution()
print(s.rob2(root))
print(s.rob2(root2))