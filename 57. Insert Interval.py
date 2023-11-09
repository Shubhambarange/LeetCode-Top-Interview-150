You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  # Initialize an empty list to store the result

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:  # If the end of newInterval is before the start of the current interval
                res.append(newInterval)  # Add newInterval to the result
                return res + intervals[i:]  # Return the result and the remaining intervals

            elif newInterval[0] > intervals[i][1]:  # If the start of newInterval is after the end of the current interval
                 res.append(intervals[i])  # Add the current interval to the result

            else:  # If there is an overlap between newInterval and the current interval
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]  # Merge the intervals

        res.append(newInterval)  # Add the merged or remaining newInterval to the result
        
        return res  # Return the final result
