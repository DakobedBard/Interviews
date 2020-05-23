class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    paths = []

    def hasPathSum(self, root, sum):
        return self.hasPathSumRecursive(root, sum)

    def hasPathSumRecursive(self,root,sum):
        if root.left == None and root.right == None:
            if sum == root.val:
                return True
            else:
                return False
        leftPath = False
        rightPath = False
        if root.left:
            leftPath = self.hasPathSumRecursive(root.left, sum - root.val,)
        if root.right:
            rightPath = self.hasPathSumRecursive(root.right, sum-root.val)

        return leftPath or rightPath


    def pathSumRecursive(self, root, sum, path ):

        if root:
            path.append(root.val)
        else:
            return
        if root.left == None and root.right == None:
            if sum == root.val:
                self.paths.append(path)
                return
            else:
                return

        leftpath = path.copy()
        rightpath = path.copy()

        if root.left:
            self.pathSumRecursive(root.left, sum - root.val, leftpath)
        if root.right:
            self.pathSumRecursive(root.right, sum-root.val, rightpath)

    def pathSum(self, root, sum):
        path = []
        self.pathSumRecursive(root, sum, path)
        return self.paths

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(2)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(1)

solution = Solution()
b = solution.pathSum(root, 9)