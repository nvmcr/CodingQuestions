class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        # Creating an adj list
        adjlist = defaultdict(list)
        for a, b in dislikes:
            adjlist[a].append(b)
            adjlist[b].append(a)
        
        def dfs(person, perCol):
            color[person] = perCol
            for nei in adjlist[person]:
                if color[nei] == perCol:
                    return False
                if color[nei] == -1:
                    if not dfs(nei, 1-perCol):
                        return False
            
            return True


        color = [-1 for _ in range(n+1)]

        for i in range(1,n+1):
            if color[i] == -1:
                if not dfs(i,0):
                    return False
        
        return True
