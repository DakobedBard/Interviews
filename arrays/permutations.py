class Solution:
    def permuteUnique(self, nums):
        n = len(nums)
        result = set()

        def backtrack(l, r, nums):
            if l == r:
                return result.add((*nums,))  # We reached the end of the recursion
                # tree
            else:
                for i in range(l, r + 1):
                    nums[l], nums[i] = nums[i], nums[l]
                    backtrack(l + 1, r, nums)
                    nums[i], nums[l] = nums[l], nums[i]

        backtrack(0, n - 1, nums)
        print(result)
        return [list(perm) for perm in result]

    def permute(self, nums):
        n = len(nums)
        result = []

        def backtrack(l, r, nums):
            if l == r:
                return result.append(list(nums))  # We reached the end of the recursion
                # tree
            else:
                for i in range(l, r + 1):
                    nums[l], nums[i] = nums[i], nums[l]
                    backtrack(l + 1, r, nums)
                    nums[i], nums[l] = nums[l], nums[i]

        backtrack(0, n - 1, nums)
        print(result)
        return result

solution = Solution()
nums = [1,2,2]
permset = solution.permuteUnique(nums)

