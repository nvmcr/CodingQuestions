class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        safe_nodes = {} # To store if a node is safe node or not

        def dfs(node):
            if node in safe_nodes:
                return safe_nodes[node]
            # Temporarily mark node as False
            safe_nodes[node] = False
            for nei in graph[node]: # Check the connected nodes
                if not dfs(nei): # We get False if there is a circle
                    return False
            safe_nodes[node] = True # If there are no connected nodes, mark them as safe
            return True
            
        res = []
        for node in range(length):
            if dfs(node):
                res.append(node)
        return res
