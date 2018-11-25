# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            res.append(str(root.val))
            return res
        if root.left:
            path = self.binaryTreePaths(root.left)
            for p in path:
                res.append(str(root.val) + '->' + p)
        if root.right:
            path = self.binaryTreePaths(root.right)
            for p in path:
                res.append(str(root.val) + '->' + p)
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
        root = nodes[1]
        root.left = nodes[2]
        root.right = nodes[3]
        root.left.right = nodes[5]
        return root

s = Solution()

root = s.makeTrees([0,1,2,3,4,5,6,7,8,9,10])

s.printTrees(root)

print(s.binaryTreePaths(root))
