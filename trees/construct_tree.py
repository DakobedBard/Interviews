class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        rootValue = preorder.pop(0)
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)
        print("rootval {} inorder Index {}".format(rootValue, inorderIndex))
        print("inorder[:inorderIndex] {}".format(inorder[:inorderIndex]))
        print("inorder[inorderIndex + 1:] {} ".format(inorder[inorderIndex + 1:]))

        root.left = self.buildTree(preorder, inorder[:inorderIndex])
        root.right = self.buildTree(preorder, inorder[inorderIndex + 1:])

        return root






preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
root= solution.buildTree(preorder, inorder)