class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # The idea is to try all combinations of adding and subtracting all jug capacities
        seen = set()
   
        def dfs(target):
            if target == targetCapacity:
                return True
            if target in seen or target < 0 or target > jug1Capacity + jug2Capacity:
                return False
            seen.add(target)
            return dfs(target+jug1Capacity) or dfs(target-jug1Capacity) or dfs(target+jug2Capacity) or dfs(target-jug2Capacity)

        return dfs(0)
