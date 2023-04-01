class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = -1 #if all 0's then this will not update throughout code
        from collections import deque
        q = deque()
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                  q.append([row,col]) #Adding 1's first because res = level

        trav = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            r,c = q.popleft()
            res = grid[r][c] # res becomes (1 + level) in each loop run
            for rtrav, ctrav in trav:
                rnew, cnew = r + rtrav, c + ctrav #traversing in all 4 directions
                if (rnew >= 0 and rnew < rows and cnew >= 0 and cnew < cols
                   and grid[rnew][cnew] == 0):
                    q.append([rnew,cnew])
                    grid[rnew][cnew] = grid[r][c] + 1 #The first level 0's becomes 2 

        return res-1 if res > 1 else -1
