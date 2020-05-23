
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pruneTree(root):

    if root == None:
        return None
    def containsOne(node):
        if not node:
            return False
        lcontains = containsOne(node.left)
        rcontains = containsOne(node.right)

        if not lcontains:
            node.left = None
        if not rcontains:
            node.right = None
        if containsOne(node.right) == False:
            node.right = None
        return node.val == 1 or lcontains or rcontains
    containsOne(root)

    return root

root = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

newroot = pruneTree(root)