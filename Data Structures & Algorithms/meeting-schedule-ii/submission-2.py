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
        max_rooms = count = 0
        for point in flatten:
            count += point[1]
            max_rooms = max(max_rooms, count)

        return max_rooms
