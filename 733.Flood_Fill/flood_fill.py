class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image) - 1
        columns = len(image[0]) - 1
        orgcolor = image[sr][sc]
        if orgcolor == color:
            return image
        def dfs(r,c):
            if r < 0 or c < 0 or r > rows or c> columns or image[r][c] != orgcolor or image[r][c] == color:
                return
            image[r][c] = color
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r,c+1)
        
        dfs(sr,sc)
        return image
