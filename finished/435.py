# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        end = - 2 ** 32
        res = 0
        intervals.sort(key = lambda i : i.end)
        for i in intervals:
            if i.start < end:
                res += 1
            else:
                end = i.end

        return res