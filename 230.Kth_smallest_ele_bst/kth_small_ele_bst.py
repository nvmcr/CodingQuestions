# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        #do inorder traversal
        def inorder(root):
            if not root: return []
            else: return (inorder(root.left)+[root.val]+inorder(root.right))
        sort_arr = inorder(root)
        print(sort_arr)
        return sort_arr[k-1] #-1 as k is 1-indexed
        '''
        #Iterative
        n, stack, curr = 0, [], root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
