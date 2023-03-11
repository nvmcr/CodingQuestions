class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Trick is to add zero at the start and end of each row
        res = [[1]]
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = [] #Stores that particular row values
            for j in range(len(res)+1): #One number more than previous row
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
