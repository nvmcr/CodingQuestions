# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # The main idea is to understand the options of splitting and not splitting
        # Declare a global variable that can be updated within recursive function
        res = 0 # Can also use a list because and it need not be declared as nonlocal in inside function

        # Return only the values without split
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # If the left and right max are negative, discard them
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            # To keep track of max value with split, update the global variable
            res = max(res, root.val + leftMax + rightMax)
            # Return without split we can only take one side of children
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res
