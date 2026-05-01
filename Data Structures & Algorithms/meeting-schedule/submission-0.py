"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for r in range(1,len(intervals)):
            prev = intervals[r-1]
            cur = intervals[r]

            if cur.start < prev.end:
                return False
        return True