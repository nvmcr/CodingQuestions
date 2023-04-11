class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # The idea is to do bfs as we need find the shortest path to reach a particular target
        # If the starting point is in deadend, we cant move
        if "0000" in deadends:
            return -1
        q = deque()
        q.append(("0000",0)) #Present lock, number of moves
        # We need to have a visit set and also deadends need to be converted to set for O(1) search
        seen = set(deadends)

        def nextlock(lock):
            children = []
            for i in range(4): # 4 because of 4 digits but need 8 outputs as we can go clock or anticlock
                nextdigit = str((int(lock[i]) + 1)%10) # %10 beacuse if we add 9 + 1 it should give 0 not 10
                children.append(lock[:i]+nextdigit+lock[i+1:])
                nextdigit = str((int(lock[i]) - 1+10)%10) # % +10 to avoid -1
                children.append(lock[:i]+nextdigit+lock[i+1:])
            return children

        while q:
            lock, res = q.popleft()
            if lock == target:
                return res
            for child in nextlock(lock):
                if child not in seen:
                    q.append((child,res+1))
                    seen.add(child)
        
        return -1
