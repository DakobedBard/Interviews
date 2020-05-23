class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#
#     def maxSumBST(self,root):
#         self.max_path_sum = float('-inf')
#         self.pathSumRecursive(root)
#         return self.max_path_sum
#     def pathSumRecursive(self, node):
#
#         if node == None:
#             return 0
#         print("Recursive call on node {} ".format(node.val) )
#         left = max(0, self.pathSumRecursive(node.left))
#         right = max(0, self.pathSumRecursive(node.right))
#
#         self.max_path_sum = max(self.max_path_sum, left+right + node.val)
#         return max(left,right) + node.val
#
#








class Solution:

    def maxSumBST(self, root):
        self.max_path_sum = float('-inf')
        self.maxPathSumRecursive(root)
        return self.max_path_sum
    def maxPathSumRecursive(self, node):

        if node == None:
            return 0
        leftsum = max(0,self.maxPathSumRecursive(node.left))
        rightsum = max(0,self.maxPathSumRecursive(node.right))
        print("I am at node {} and my lsum is {} and my rsum is {} ".format(node.val, leftsum, rightsum) )
        self.max_path_sum = max(self.max_path_sum, leftsum+rightsum+node.val)

        return max(leftsum, rightsum) + node.val



root = TreeNode(-5)
root.left = TreeNode(-1)
root.right = TreeNode(-2)
solution = Solution()
print("The maximum path sum of trees in this binary tree is {}".format(solution.maxSumBST(root)))