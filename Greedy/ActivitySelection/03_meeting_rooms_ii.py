"""MEETING ROOMS II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation: We need two meeting rooms:
- Room 1: [0,30]
- Room 2: [5,10],[15,20]

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti < endi <= 10^6

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def min_meeting_rooms(intervals):
    start, end = [], []
    for interval in intervals:
        start.append(interval[0])
        end.append(interval[1])
    start = sorted(start)
    end = sorted(end)

    count, max_count = 0, 0
    i, j = 0, 0

    while i < len(start):
        if start[i] < end[j]:
            count += 1
            max_count = max(max_count, count)
            i += 1
        else:
            count -= 1
            j += 1
    return max_count