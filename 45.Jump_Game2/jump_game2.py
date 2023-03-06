class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS
        res = 0 # This tells us the Level in bfs. level~jumps
        l=r=0 #Will have l and r for the first and last idx pos in a particular level

        while r < len(nums) - 1: # Reached the last index
            last_idx = 0 #Farthest index in that particular level
            for i in range(l, r+1):
                last_idx = max(last_idx, i + nums[i]) #Farthest that can be reached
            l = r+1
            r = last_idx
            res+=1
        return res
