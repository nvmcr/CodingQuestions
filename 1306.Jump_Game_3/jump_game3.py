class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # The idea is to do a simple dfs or bfs and just traverse through the array
        q = [start]
        visit = set()

        while q:
            i = q.pop()
            if arr[i] == 0: return True
            visit.add(i)
            next1, next2 = i + arr[i], i-arr[i]
            if next1 < len(arr) and next1 not in visit:
                q.append(next1)
            if next2>=0 and next2 not in visit:
                q.append(next2)
                
        return False
