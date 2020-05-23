class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    if not root:
        return 0
    ldepth= maxDepth(root.left)
    rdepth = maxDepth(root.right)
    return max(ldepth, rdepth) +1

class Solution:
    def maxDiameter(self,root):
        self.maxpaths = 0
        def maxDepth(node):
            if not node:
                return 0
            maxl = maxDepth(node.left)
            maxr = maxDepth(node.right)
            maxd = max(maxl, maxr) +1
            self.maxpaths = max(self.maxpaths, maxl + maxr + 1)
            return maxd
        maxDepth(root)
        return self.maxpaths - 1

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.right.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.left.left.left = TreeNode(1)
root.left.right.right = TreeNode(1)
root.left.right.right.right = TreeNode(1)
root.left.right.right.right.right = TreeNode(1)
root.left.right.right.right.right.right = TreeNode(1)
solution = Solution()

print("The maximum depth of the tree is {} ".format(maxDepth(root)))
print("The maximum length of the path of the tree is {} ".format(solution.maxDiameter(root)))