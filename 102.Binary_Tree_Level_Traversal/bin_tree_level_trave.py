# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            res.append([node.val for node in queue]) #Using append because seperate lists are required
            nodes = []
            for node in queue:
                nodes.extend([node.left, node.right])
            queue.clear()
            for child in nodes:
                if child:
                    queue.append(child)
        return res

""" Prints in sepreate lists
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        queue = [root]
        result = []
        idx = 0
        while idx < len(queue):
            node = queue[idx]
            result.append([node.val])
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            idx += 1
        print(result)
        return result
"""
