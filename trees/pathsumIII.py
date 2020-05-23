class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def pathSum(self, node: TreeNode, sum: int) -> int:

        def dfs(node: TreeNode, target: int, parent_vals: list) -> int:
            if node is None:
                return 0

            count = 0

            # Count one path if this node by itself is the correct sum
            if node.val == target:
                count += 1

            # Count any correct path sums starting from this node up through its parents
            total = node.val
            for parent in parent_vals:
                total += parent
                if total == target:
                    count += 1

            # Recursively count any correct path sums starting in either child node
            count += dfs(node.left, target, [node.val] + parent_vals)
            count += dfs(node.right, target, [node.val] + parent_vals)

            # Return the total count for this node and its children
            return count

        return dfs(node, sum, [])

        # root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(1)
# root.right = TreeNode(3)
#
# solution = Solution()
# print("There are {} ways to sum to {} in this tree ".format(solution.pathSum(root, 4), 4))


# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(-3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.left.left.left = TreeNode(3)
# root.left.left.right = TreeNode(-2)
# root.left.right.right = TreeNode(1)
# root.right.right = TreeNode(11)
# solution = Solution()

root = TreeNode(10)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
root.right.right = TreeNode(11)
solution = Solution()


print("There are {} ways to sum to {} in this tree ".format(solution.pathSum(root, 8), 8))