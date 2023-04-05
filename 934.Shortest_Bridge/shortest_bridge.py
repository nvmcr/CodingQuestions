class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #smallest number of flips to connect two islands is nothing but finding shortest distance between two islands
        rows, cols = len(grid), len(grid[0])
        q=deque()
        visit = set()

        direct = [[1,0],[-1,0],[0,1],[0,-1]]

        def invalid(r,c):
            return True if (min(r,c) < 0 or max(r,c) >= rows) else False

        def dfs(r,c):
            if invalid(r,c) or grid[r][c] != 1 or (r,c) in visit:
                return
            visit.add((r,c))
            for dr, dc in direct:
                dfs(r+dr,c+dc)

        def bfs():
            res, q=0, deque((visit))
            while q:
                for level in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        newr, newc = r+dr, c+dc
                        if invalid(newr, newc) or (newr, newc) in visit:
                            continue
                        if grid[newr][newc] == 1:
                            return res
                        q.append((newr,newc))
                        visit.add((newr,newc))
                res += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # We cant add all 1s, we only need one island so use dfs
                    dfs(row,col)
                    return bfs()
        # Now do bfs to find shortest path to next 1s that are not in visit set
        
