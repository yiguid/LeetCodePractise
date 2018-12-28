# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l = len(intervals)
        if l <= 1:
            return intervals

        intervals.sort(key = lambda x: x.start)
        ret = [intervals[0]]
        for i in range(1, l):
            interval = intervals[i]
            if ret[-1].end >= interval.start:
                ret[-1].end = max(ret[-1].end, interval.end)
            else:
                ret.append(interval)
        return ret