class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Will do a general bfs with a length attached
        gridlen = len(grid)
        q = deque([(0,0,1)]) #Pos and length
        visit = set()

        direct = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,-1],[-1,1],[1,1]] #8 directions
        while q:
            r, c, length = q.popleft()
            if min(r,c) < 0 or max(r,c) >= gridlen or grid[r][c] == 1:
                continue #ignore
            if r==gridlen-1 and c==gridlen-1:
                return length
            for dr,dc in direct:
                if (r+dr,c+dc) not in visit:
                    q.append((r+dr,c+dc,length+1))
                    visit.add((r+dr,c+dc))
        return -1
