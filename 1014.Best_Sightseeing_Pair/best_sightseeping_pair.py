class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # We need to maintain high v[i] + i
        best_i, res = 0, 0
        for i, v in enumerate(values):
            res = max(res, v - i + best_i) #same formula just i in place of j
            best_i = max(best_i, v + i)
        return res
