class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        stack = [0]
        def dfs(stack):
            if stack[-1] == len(graph)-1:#Reched node n-1
                res.append(stack)
            for child in graph[stack[-1]]:
                dfs(stack+[child])
        dfs(stack)
        return res
