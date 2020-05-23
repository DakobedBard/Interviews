class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def findBottomLeftValue(root):

    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return node.val


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print("The leftmost value of the bottom row of this tree is {}".format(findBottomLeftValue(root)))