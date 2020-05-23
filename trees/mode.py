class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

class Solution:
    def traverse(self, root):
        if not root:
            return
        else:
            self.mem[root.val] += 1
            self.traverse(root.left)
            self.traverse(root.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.mem = defaultdict(int)
        ans = []
        if not root: return []
        self.traverse(root)
        keyList = sorted(self.mem, key=lambda x:-self.mem[x])
        maxVal = self.mem[keyList[0]]
        for key in keyList:
            if self.mem[key]==maxVal:
                ans.append(key)
        return ans

root = TreeNode(10)
root.left = TreeNode(6)
root.left.right =TreeNode(8)
root.left.right.left = TreeNode(6)
root.right = TreeNode(12)


# root = TreeNode(20)
# root.right = TreeNode(30)
# root.right.left = TreeNode(20)
# root.right.left.right = TreeNode(20)
# root.right.left.right.right = TreeNode(25)
# root.right.left.right.right.left = TreeNode(20)
# root.right.left.right.right.right=TreeNode(28)
#
# root.left= TreeNode(10)
# root.left.left=TreeNode(5)
# root.left.right=TreeNode(15)
# root.left.right.left = TreeNode(10)
# root.left.right.right=TreeNode(15)
# root.left.right.left.right = TreeNode(12)
# root.left.right.right.right =TreeNode(18)
# root.left.right.right.right.left = TreeNode(16)


solution = Solution()
freqs = solution.findMode(root)
# print("The result is  {}".format(solution.findMode(root)))