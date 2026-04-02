"""ACTIVITY SELECTION PROBLEM

Given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

Example 1:
Input: start = [1, 3, 0, 5, 8, 5], finish = [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: A person can perform at most four activities: {0, 1, 3, 4}

Example 2:
Input: start = [10, 12, 20], finish = [20, 25, 30]
Output: 3
Explanation: A person can perform all three activities.

Constraints:
- 1 <= n <= 10^5
- 0 <= start[i] < finish[i] <= 10^6

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def activity_selection(start, finish):
    pass