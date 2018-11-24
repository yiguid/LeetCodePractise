# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def findPath(root, sum):
            res = 0
            if not root:
                return res
            if root.val == sum:
                res = 1
            if root.left:
                res += findPath(root.left, sum - root.val)
            if root.right:
                res += findPath(root.right, sum - root.val)
            return res
        res = 0
        if not root:
            return res
        res = findPath(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res

    def makeTrees(self, data):
        nodes = []
        for n in data:
            node = TreeNode(n)
            nodes.append(node)
        root = self.constructTress(nodes)
        return root

    def printTrees(self, root):
        if root != None:
            self.printTrees(root.left)
            print(root.val)
            self.printTrees(root.right)

    def constructTress(self, nodes):
        root = nodes[10]
        root.left = nodes[5]
        root.right = TreeNode(-3)
        root.left.left = nodes[3]
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right = nodes[2]
        root.left.right.right = nodes[1]
        root.right.right = TreeNode(11)
        return root

s = Solution()

root = s.makeTrees([0,1,2,3,4,5,6,7,8,9,10])

# s.printTrees(root)

print((s.pathSum(root,8)))