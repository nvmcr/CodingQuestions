class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            length = len(res)
            temp = [0] + res + [0]
            res = []
            for j in range(length + 1):
                res.append(temp[j]+temp[j+1])
        return res
