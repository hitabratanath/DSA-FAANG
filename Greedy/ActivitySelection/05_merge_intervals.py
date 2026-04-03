"""MERGE INTERVALS

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def merge(intervals):
    if len(intervals) < 2: return intervals

    intervals.sort()
    stk = [intervals[0]]
    for curr_start, curr_end in intervals[1:]:
        prev_start, prev_end = stk.pop()
        if curr_start >= prev_start and curr_start <= prev_end:
            stk.append([prev_start, max(prev_end, curr_end)])
        else:
            stk.append([prev_start, prev_end])
            stk.append([curr_start, curr_end])
    return stk