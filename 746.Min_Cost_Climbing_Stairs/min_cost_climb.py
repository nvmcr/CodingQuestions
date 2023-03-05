class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        # Start from the end
        # Changing the cost within array
        # Need not to change last two costs in the array as any path should reach one of the two.
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1], cost[i+2]) #c[i] = min((c[i] + c[i+1]), (c[i]+c[i+2]))
        res = min(cost[0], cost[1]) #we can start from index 0 or 1
        return res 
