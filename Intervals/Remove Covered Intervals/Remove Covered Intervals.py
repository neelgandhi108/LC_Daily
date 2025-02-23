class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by small start and big end
        intervals = sorted(intervals,key = lambda x : (x[0],-x[1]))
        prev_start , prev_end = intervals[0]
        res = len(intervals)
        for start, end in intervals[1:]:
            if prev_end >= end:
                res -= 1
            else:
                prev_start = start
                prev_end = end
        return res