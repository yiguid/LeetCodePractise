# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
            



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
        root = nodes[4]
        root.left = nodes[2]
        root.right = nodes[7]
        root.left.left = nodes[1]
        root.left.right = nodes[3]
        root.right.left = nodes[6]
        root.right.right = nodes[9]
        return root

s = Solution()

root = s.makeTrees([0,1,2,3,4,5,6,7,8,9,10])

# s.printTrees(root)

s.printTrees(s.invertTree(root))
