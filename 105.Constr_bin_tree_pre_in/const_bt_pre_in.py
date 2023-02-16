# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            root_ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_ind])
            root.left = self.buildTree(preorder,inorder[:root_ind])
            root.right = self.buildTree(preorder,inorder[root_ind + 1:])
            return root
        
