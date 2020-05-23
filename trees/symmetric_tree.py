class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return "val: {}".formatself.val
def isSymmetric(root):
    isMirror(root.left, root.right)


def isMirror(t1, t2):
    if t1 == None and t2 == None: return True
    if t1 == None or t2 == None: return False

    return isMirror(t1.left, t1.right) and   isMirror(t2.left, t2.right)



def isSymmetridIterative(root):
    if root == None:
        return True
    if not root.left and not root.right:
        return True

    stack = [root]
    while stack:
        newstack = []
        while stack:
            current = stack.pop(0)
            if current:
                newstack.append(current.left)
                newstack.append(current.right)

        if len(newstack) % 2 != 0:

            return False
        i = 0
        j = len(newstack) -1
        while i <= j:
            if newstack[i] and newstack[j] and newstack[i].val != newstack[j].val:
                return False
            elif not newstack[i] and not newstack[j]:
                i += 1
                j -= 1

            elif not newstack[i] or  not newstack[j]:
                return False
            else:
                i += 1
                j -= 1

        stack = newstack

    return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(2)
root.right.left = TreeNode(4)
print('This tree is symmetic {} '.format(isSymmetridIterative(root)))