class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # The problem needs the knowledge of integral image.
        # In integral image, each element is the sum of all elements that came before it.
        rows, cols = len(mat), len(mat[0])
        IntegralImage = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(0, rows):
            presum = 0
            for c in range(0, cols):
                presum += mat[r][c]
                IntegralImage[r][c] = presum # Computes sum of before elements in that col 
                if r > 0:
                    IntegralImage[r][c] += IntegralImage[r-1][c] # Gives all before elements sum 
        
        answer = [[0 for _ in range(cols)] for _ in range(rows)]
        # To get the sum of elements in a rectangular block ABCD where A,B are in same row and C,D in same row; equation is A + D - B - C.
        for r in range(rows):
            for c in range(cols):
                minrow, maxrow = max(0, r-k), min(rows-1, r+k) # Shouldnt exceed limits
                mincol, maxcol = max(0, c-k), min(cols-1, c+k)
                # We are located at D, should calculate A+D-B-C
                answer[r][c] = IntegralImage[maxrow][maxcol] #D
                if minrow > 0:
                    answer[r][c] -= IntegralImage[minrow-1][maxcol] #B
                if mincol >0:
                    answer[r][c] -= IntegralImage[maxrow][mincol-1] #C
                if minrow > 0 and mincol >0:
                    answer[r][c] +=  IntegralImage[minrow-1][mincol-1] #A
        return answer
