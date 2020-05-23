class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelorder(root):
    if not root:
        return root
    stack = [root]
    while stack:
        level = []
        new_stack = []
        while stack:
            node = stack.pop(0)
            level.append(node.val)
            if node.left:
                new_stack.append(node.left)
            if node.right:
                new_stack.append(node.right)
            stack = new_stack
    return level

root = TreeNode(2)
root.right = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
level = levelorder(root)
