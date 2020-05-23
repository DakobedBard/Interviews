
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):

        result = []

        def dfs(node, path):
            print("The path is {} and the current node is {}".format(path, node.val))
            if not node.left and not node.right:
                path.append(str(node.val))
                result.append('->'.join(path))
            leftpath = path.copy()
            leftpath.append(str(node.val))
            rightpath = path.copy()
            rightpath.append(str(node.val))

            if node.left:
                dfs(node.left, leftpath)
            if node.right:
                dfs(node.right, rightpath)
        dfs(root, [])
        return result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

solution = Solution()
paths = solution.binaryTreePaths(root)