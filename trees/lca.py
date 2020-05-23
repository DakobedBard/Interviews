class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(5)

def isbst(root):
    if root == None:
        return True
    if root.left and root.left.info > root.info:
        return False
    elif root.right and root.right.info < root.info :
        return False
    return isbst(root.left) and isbst(root.right)

print("The tree is a bst " + str(isbst(root)))

def iterative_lca(root, v1, v2):
    if v1 > v2:
        v1, v2 = v2, v1

    while True:
        if v1 < root.info and v2 < root.info:
            root = root.left
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            return(root)


def lca(root, v1, v2):
    if v1 < root.info< v2:
        return root .info
    elif v1 < root.info and v2 < root.info:
        return lca(root.left, v1, v2)
    else:
        return lca(root.right, v1, v2)

print("The lca of " + str(lca(root, 1,3)))