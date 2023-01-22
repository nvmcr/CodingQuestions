class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the given intervals by their starting element
        intervals.sort() # or intervals.sort(key = lambda inter: inter[0])

        result = [intervals[0]] #starting without empty because our algo needs prev list
        for start, end in intervals[1:]:
            prevEnd = result[-1][1]
            if start <= prevEnd:
                result[-1][1] = max(prevEnd, end)
            else:
                result.append([start, end])
        return result
