"""MEETING ROOMS

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: [0,30] and [5,10] overlap, [0,30] and [15,20] overlap

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti < endi <= 10^6

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

def can_attend_meetings(intervals):
    if len(intervals) < 2: return True

    intervals.sort()
    end = intervals[0][1]
    for a, b in intervals[1:]:
        if a < end: return False
        end = b
    return True