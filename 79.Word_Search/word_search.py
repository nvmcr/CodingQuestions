class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        #backtracking
        def dfs(r, c, i):
            if i == len(word): #If all letters are done
                return True
            #all false cases
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c] or (r,c) in visited):
                return False
            #If a letter is visited, add it to set so that same letter may not be used again
            visited.add((r,c))
            #check all 4 sides
            ans = (dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or
                    dfs(r,c-1,i+1) or dfs(r,c+1,i+1))
            visited.remove((r,c)) #For next loop
            return ans
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c,0) is True:
                    return True
        return False
