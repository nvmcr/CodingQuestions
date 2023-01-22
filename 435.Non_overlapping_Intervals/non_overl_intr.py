class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd: #They are not overlapping
                prevEnd = end
            else:
                count += 1
                prevEnd = min(end, prevEnd)
        return count
