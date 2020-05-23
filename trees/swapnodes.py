class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def inorder(node):
    if node ==None:
        return
    inorder(node.left)
    print("data {}".format(node.data))
    inorder(node.right)


input_ = [[]]

