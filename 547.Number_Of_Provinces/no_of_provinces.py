class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        res = 0

        def dfs(connectedcity):
            for city, Isconnection in enumerate(connectedcity):
                if Isconnection and city not in visit:
                    visit.add(city)
                    dfs(isConnected[city])

        for city, connectedcity in enumerate(isConnected):
            if city not in visit:
                res += 1
                visit.add(city)
                dfs(connectedcity)
        return res
