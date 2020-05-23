class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def mergeTrees(t1, t2):
    if t1 == None:
        return t2
    if t2 == None:
        return t1
    t1.val += t2.val
    t1.left = mergeTrees(t1.eft, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1

def mergeTreesIterative(t1, t2):
    if t1 == None:
       return t2




tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(5)

tree2= TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)
tree2.right.right = TreeNode(7)

