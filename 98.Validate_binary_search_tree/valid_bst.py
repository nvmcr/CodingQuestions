# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(root, left, right):
            if not root:
                return True
            elif not (left < root.val and root.val < right):
                return False
            return validBST(root.left, left, root.val) and validBST(root.right, root.val, right)
        return validBST(root, left=-math.inf, right=math.inf)
