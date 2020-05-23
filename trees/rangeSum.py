class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumRecursive(self,node, L,R, parentval):
        if node:
            print("I'm at node {} and my parentsval is {}".format(node.val, parentval) )
        if not node or parentval <= L or parentval >= R:
            return 0
        print("In recursive call and my value is {}".format(node.val) )

        if node.val >= L or node.val <= R:
            self.rsum += node.val
        self.rangeSumRecursive(node.left, L,R, node.val)
        self.rangeSumRecursive(node.right, L,R,y node.val)

    def rangeSum(self,root, L, R):
        if not root:
            return 0
        self.rsum = 0
        self.rangeSumRecursive(root, L, R, root.val)

        return self.rsum

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
solution = Solution()
L = 7
R = 15
print("The sum of all values between {} and {} of this tree is {}".format(L, R, solution.rangeSum(root, L, R)))