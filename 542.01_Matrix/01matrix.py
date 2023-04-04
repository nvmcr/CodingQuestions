class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        q = deque()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append([row,col])
                else:
                    mat[row][col] = -1
        direct = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            r, c = q.popleft()
            for dr, dc in direct:
                newr, newc = r+dr, c+dc
                if 0<=newr<rows and 0<=newc<cols and mat[newr][newc] == -1:
                    mat[newr][newc] = mat[r][c] + 1
                    q.append([newr, newc])
        
        return mat
