class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    total = 0
    def reverseInOrder(self,root):

        if root == None:
            return
        self.reverseInOrder(root.right)
        print(root.val + self.total)
        self.total += root.val
        root.val = self.total
        self.reverseInOrder(root.left)
        return root

    def greaterTreeIterative(self, root):
        total = 0
        node = root
        stack = []
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total



root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
# root.right.right = TreeNode(15)

solution = Solution()
newroot = solution.reverseInOrder(root)