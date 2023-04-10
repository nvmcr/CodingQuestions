class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = deque()
        q.append([0, 0, False]) #[no.of jumps, curr pos, Did I jump back]
        forbid = set(forbidden) #O(1) search for sets
        visit = set()
        visit.add((0,False))
        while q:
            res, curr, back = q.popleft()
            if curr == x:
                return res
            next1, next2 = curr+a, curr-b
            if next1 not in forbid and next1-b<=x and (next1,False) not in visit:
                q.append([res+1,next1,False])
                visit.add((next1,False))
            if next2 not in forbid and next2>0 and not back and (next2,True) not in visit:
                q.append([res+1,next2,True])
                visit.add((next2,True))
        return -1
            
