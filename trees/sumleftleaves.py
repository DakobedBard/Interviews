

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        self.lsum = 0
        self.sumOfLeftLeavesRecursive(root, False)
        return self.lsum
    def sumOfLeftLeavesRecursive(self, node, isleft):
        if not node:
            return
        if not node.left and not node.right:
            if isleft:
                self.lsum += node.val

        self.sumOfLeftLeavesRecursive(node.left, True)
        self.sumOfLeftLeavesRecursive(node.right, False)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print("The lsum of the tree is {} ".format(solution.sumOfLeftLeaves(root)))