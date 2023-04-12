class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # The idea is to increment a score by 1 for every person one trusts.
        # Thus a judge is someone with a score of n-1(everyone trusts him without including him)
        # We also need to decrement if a person trust someone else, because judge shouldn't trust others
        if not trust:
            return 1
        scores = [0 for i in range(n+1)]
        
        for a, b in trust:
            scores[b] += 1
            scores[a] -= 1
        
        for person, score in enumerate(scores):
            if score == n-1:
                return person
        return -1
