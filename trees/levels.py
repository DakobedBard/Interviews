class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    levels = []
    stack = [root]
    while stack:
        level = []
        for element in stack:
            level.append(element.val)
        levels.append(level)
        newstack = []
        while stack:
            current = stack.pop()
            if current.left:
                newstack.append(current.left)
            if current.right:
                newstack.append(current.right)
        print(newstack)
        stack = newstack
    return levels
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

levels = levelOrderTraversal(root)