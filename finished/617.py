# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees1(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t2 != None:
            if t1 != None:
                root = t1
                t1.val += t2.val
                root.left = self.mergeTrees(t1.left, t2.left)
                root.right = self.mergeTrees(t1.right, t2.right)
            else:
                root = t2
                root.left = self.mergeTrees(None, t2.left)
                root.right = self.mergeTrees(None, t2.right)
        else:
            if t1 != None:
                root = t1
                root.left = self.mergeTrees(t1.left, None)
                root.right = self.mergeTrees(t1.right, None)
            else:
                return None
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
            print(root.val)
            self.printTrees(root.left)
            self.printTrees(root.right)

    def constructTress(self, nodes):
        root = nodes[0]
        root.left = nodes[1]
        root.right = nodes[2]
        root.left.left = nodes[3]
        root.left.right = nodes[4]
        root.right.left = nodes[5]
        root.right.right = nodes[6]
        return root

s = Solution()

root = s.makeTrees([1,2,3,4,5,6,7])

s.printTrees(root)

s.printTrees(s.mergeTrees(root,root))



