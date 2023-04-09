class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # The idea is if we do dfs/bfs, increase the count if we come across the nodes not directed towards parent
        
        self.res = 0
        # We can not traverse to neighbors if the edges are directed towards parent(0) so will buils adj_list for undirected edges
        graph = defaultdict(list)
        roads = set()
        visit = set()
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            # converting connections to set as look up time is O(1) for sets (O(n) for lists)
            roads.add((a,b))
        
        def dfs(city):
            for nei in graph[city]:
                if nei in visit:
                    continue
                if (nei,city) not in roads: # nei=1,city=0 (1,0) wont be in edge only (0,1)
                    # Means direction is opposite of city(parent)
                    self.res += 1
                visit.add(nei)
                dfs(nei)
            
        visit.add(0)
        dfs(0)

        return self.res
