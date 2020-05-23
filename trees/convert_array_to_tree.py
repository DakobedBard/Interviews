from math import ceil

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    if not nums:
        return None

    left = 0
    right = len(nums)-1
    mid = int(left + (right-left)/2)

    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid+1:])

    return node

arr = [-10, -3, 0,5,9]
root = sortedArrayToBST(arr)