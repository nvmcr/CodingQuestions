class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(u,ucol):
            color[u] = ucol
            for v in graph[u]:
                if color[v] == ucol:
                    return False
                if color[v] == -1:
                     if not dfs(v, 1-ucol):
                         return False
            
            return True


        n = len(graph) #number of nodes
        color = [-1 for _ in range(n)]
        for i in range(n):
            if color[i] == -1:
                if not dfs(i,0):
                    return False
        
        return True
