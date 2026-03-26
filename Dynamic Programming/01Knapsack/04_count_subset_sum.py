"""COUNT OF SUBSETS WITH GIVEN SUM

Given an array arr[] of non-negative integers and an integer sum, find the count of subsets 
of the array with sum equal to the given sum.

Example 1:
Input: arr = [2, 3, 5, 6, 8, 10], sum = 10
Output: 3
Explanation: Subsets are {2, 3, 5}, {2, 8}, {10}.

Example 2:
Input: arr = [1, 2, 3, 3], sum = 6
Output: 3
Explanation: Subsets are {1, 2, 3}, {1, 2, 3}, {3, 3}.

Example 3:
Input: arr = [1, 1, 1, 1], sum = 2
Output: 6
Explanation: All combinations of two 1's.

Constraints:
- 1 <= arr.length <= 100
- 0 <= arr[i] <= 100
- 1 <= sum <= 10^4
"""

from functools import lru_cache

def count_subset_given_sum(arr, sm, N):
    arr = tuple(arr)

    @lru_cache(None)
    def helper(s, n):
        if s == 0:
            return 1
        if n == 0:
            return 0
        
        if arr[n - 1] <= s:
            return helper(s - arr[n - 1], n - 1) + helper(s, n - 1)
        return helper(s, n - 1)
    return helper(sm, N)