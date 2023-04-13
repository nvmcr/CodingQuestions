class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Any edge that doesn't have an incoming edge should be in result
        res = set()
        for num in range(n):
            res.add(num)
        for a, b in edges:
            if b in res:
                res.remove(b)
        return res
        
        
        
        '''
        score = [0 for _ in range(n)]
        for a, b in edges:
            score[b] = 1
        res = []
        for a in range(n):
            if score[a] == 0:
                res.append(a)
        return res
        '''
