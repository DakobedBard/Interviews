class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rightSideView(root):
    rightmost = []
    queue = [root]
    while queue:
        size = len(queue)
        for i in range(size):
            current = queue.pop(0)
            if i == size-1:
                rightmost.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return rightmost

root = TreeNode(1)
root.left= TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
v = rightSideView(root)