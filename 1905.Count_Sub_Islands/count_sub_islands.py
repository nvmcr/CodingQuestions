class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        count = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid2[r][c] != 1:
                return
            grid2[r][c] = 0
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        #Remove all islands in grid2 that are not in grid 1
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    count += 1
                    dfs(row, col)
        return count
