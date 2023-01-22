class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        pac, atl = set(), set() #Visited sets

        def dfs(r,c,visitSet,prevHeight):
            if ((r,c) in visitSet or 
                r<0 or c<0 or r>rows-1 or c>cols-1 or 
                heights[r][c]<prevHeight):
                return 
            visitSet.add((r,c))
            dfs(r+1, c, visitSet, heights[r][c])
            dfs(r-1, c, visitSet, heights[r][c])
            dfs(r, c+1, visitSet, heights[r][c])
            dfs(r, c-1, visitSet, heights[r][c])

        #Doing top and bottom first
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows-1, col, atl, heights[rows-1][col])
        #left and right
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols-1, atl, heights[row][cols-1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
