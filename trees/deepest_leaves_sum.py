class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum( root):
    if root == None:
        return 0
    levels = []
    queue = [root]
    while queue:
        levelsum =0
        newqueue = []
        while queue:
            node = queue.pop(0)
            if node.left:
                newqueue.append(node.left)
            if node.right:
                newqueue.append(node.right)
            levelsum += node.val
        queue = newqueue
    return levelsum


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)

levels = deepestLeavesSum(root)