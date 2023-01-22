class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,total,stack):
            if total == target:
                res.append(stack.copy())
                return
            if total > target or i >= len(candidates):
                return

            stack.append(candidates[i])
            dfs(i,total+candidates[i],stack)
            stack.pop()
            dfs(i+1,total,stack)
        
        dfs(0,0,[])
        return res
