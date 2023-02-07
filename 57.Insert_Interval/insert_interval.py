class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # There are 3 cases
        for i in range(len(intervals)):
            #If there is no overlap and the new Interval should be just added at start of list
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            #Else if there is no overlap and new Interval comes after present interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: #there is an overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                #Dont append to the result until loop is done
        #Loop is done and didnt return from first case of loop, so add newInterval
        res.append(newInterval)
        return res
