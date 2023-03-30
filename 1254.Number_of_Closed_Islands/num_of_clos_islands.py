class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cloisl = 0

        def dfs(r, c):
            if r < 0 or c<0 or r>=rows or c>=cols or grid[r][c]!= 0:
                return
            grid[r][c] = 2
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        #Will update the border elements before starting a count
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and (row in [0, rows-1] or col in [0, cols-1]):
                    dfs(row, col)

        for row in range(1,rows-1):
            for col in range(1,cols-1):
                if grid[row][col] == 0:
                    cloisl += 1
                    dfs(row,col)

        return cloisl
