class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def diameter(self,root):
        self.maxpath = 0
        if root == None:
            return 0
        def maxDepthRecursive(node):
            if not node: return 0
            maxl = 0
            maxr = 0
            if node.left:
                maxl = maxDepthRecursive(node.left)
            if node.right:
                maxr = maxDepthRecursive(node.right)
            self.maxpath = max(self.maxpath, maxl + maxr + 1)
            return max(maxl, maxr) + 1

        maxDepthRecursive(root)
        return self.maxpath
solution = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)


print("The maximum path is {} ".format(solution.diameter(root)))