Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Check if the list of intervals is empty or contains only one interval
        if len(intervals) <= 1:
            return intervals

        # Sort the intervals based on the starting value of each interval
        intervals.sort(key=lambda x: x[0])

        # Initialize the result list and a newInterval with the first interval
        res = []
        newInterval = intervals[0]

        # Add the newInterval to the result list
        res.append(newInterval)

        # Iterate through the sorted intervals
        for interval in intervals:
            # If the current interval overlaps with the newInterval, merge them
            if interval[0] <= newInterval[1]:
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                # If the current interval does not overlap, start a new newInterval
                newInterval = interval
                res.append(newInterval)

        # Return the merged intervals
        return res
