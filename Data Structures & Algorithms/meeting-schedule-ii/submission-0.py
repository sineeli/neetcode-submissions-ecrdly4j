"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        flatten = []

        for interval in intervals:
            flatten.append((interval.start, 1))
            flatten.append((interval.end, -1))
        
        flatten.sort()

        count = 0
        max_rooms = 0
        for t in flatten:
            count += t[1]
            max_rooms = max(count, max_rooms)

        return max_rooms


