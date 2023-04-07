class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Just two main ideas
        # 1. We need atleast n-1 connections(edges) to connect n nodes
        if len(connections) < n-1:
            return -1
        # 2. If there are 'c' conencted groups then we need 'c-1' moves to connect all groups.
        # So find no.of groups

        visit = set()
        c = 0 #num of connected groups

        #since given connections not in type of adjacency list, will make into adjacency list
        adj_list = [[] for _ in range(n)]
        for i, j in connections:
            adj_list[i].append(j)
            adj_list[j].append(i)

        def dfs(node):
            for connected_node in adj_list[node]:
                if connected_node not in visit:
                    visit.add(connected_node)
                    dfs(connected_node)

        for node in range(n):
            if node not in visit:
                c += 1
                visit.add(node)
                dfs(node)
        
        return c-1
