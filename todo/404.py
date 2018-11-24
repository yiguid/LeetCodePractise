# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if not root:
            return sum
        if root.left:
            if not root.left.left and not root.left.right:
                sum += root.left.val
            else:
                sum += self.sumOfLeftLeaves(root.left)

        if root.right:
            sum += self.sumOfLeftLeaves(root.right)
        return sum


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
        root = nodes[3]
        root.left = nodes[9]
        root.right = nodes[20]
        root.right.left = nodes[15]
        root.right.right = nodes[7]
        return root

s = Solution()

root = s.makeTrees([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

s.printTrees(root)
print(s.sumOfLeftLeaves(root))
