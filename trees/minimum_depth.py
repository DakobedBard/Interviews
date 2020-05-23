class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minimumDepth(root):

    if root == None:
        return 0
    stack = [root]
    depth = 0
    while stack:
        newstack = []
        depth +=1
        while stack:
            current = stack.pop()
            if not current.left and not current.right:
                return depth

            if current.left:
                newstack.append(current.left)
            if current.right:
                newstack.append(current.right)

        stack = newstack




def maximumDepth(root):
    if root == None:
        return 0
    def maxDepthRecursive(root, depth):
        if not root.left and not root.right:
            return depth
        maxl = 0
        maxr = 0
        if root.left:
            maxl = maxDepthRecursive(root.left, depth+1)
        if root.right:
            maxr = maxDepthRecursive(root.right, depth+1)

        return max(maxl, maxr)

    return maxDepthRecursive(root,1)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(5)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)

print("The minimum depth is {} ".format(minimumDepth(root)))
print("The maximum depth is {} ".format(maximumDepth(root)))