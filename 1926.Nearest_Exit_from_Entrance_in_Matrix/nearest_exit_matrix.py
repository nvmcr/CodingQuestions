class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        er, ec = entrance
        q = deque([(er,ec,0)]) #distance is 0
        visit = set((er,ec))
        direct = [[0,1],[0,-1],[1,0],[-1,0]]

        while q:
            r, c, d = q.popleft()

            if (r == 0 or r==rows-1 or c==0 or c==cols-1) and (r,c) != (er,ec): #If on border
                return d
            
            for dr, dc in direct:
                newr, newc = r+dr, c+dc
                if 0<=newr<rows and 0<=newc<cols and maze[newr][newc] != '+' and (newr,newc) not in visit:
                    q.append((newr,newc,d+1))
                    visit.add((newr,newc))
        
        return -1
        
