class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # We need two cities to check rank
        # Changing into adj list
        connections = defaultdict(list)
        for a, b in roads:
            connections[a].append(b)
            connections[b].append(a)
        res = 0
        for city1 in range(n):
            for city2 in range(city1+1,n):
                dirConnect = 1 if city1 in connections[city2] else 0
                rank = len(connections[city1]) + len(connections[city2]) - dirConnect
                res = max(res, rank)
            
        return res
