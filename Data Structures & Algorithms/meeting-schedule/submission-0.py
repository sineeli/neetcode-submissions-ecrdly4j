"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda k: k.start)
        if not intervals:
            return True
        if len(intervals) == 1:
            return True
        i = 1

        while i < len(intervals):
            if intervals[i].start < intervals[i-1].end:
                return False
            i += 1
        
        return True
        