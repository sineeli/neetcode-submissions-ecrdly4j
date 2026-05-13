class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        intervals.insert(left, newInterval)
        new_intervals = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= new_intervals[-1][1]:
                new_intervals[-1][1] = max(interval[1], new_intervals[-1][1])
            else:
                new_intervals.append(interval)
        
        return new_intervals


        
