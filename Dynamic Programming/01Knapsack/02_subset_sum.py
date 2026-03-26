"""SUBSET SUM PROBLEM

Given an array of non-negative integers and a target sum, determine if there exists a subset 
of the array with sum equal to the given target.

Example 1:
Input: arr = [3, 34, 4, 12, 5, 2], sum = 9
Output: true
Explanation: Subset {4, 5} has sum 9.

Example 2:
Input: arr = [3, 34, 4, 12, 5, 2], sum = 30
Output: false
Explanation: No subset has sum 30.

Example 3:
Input: arr = [1, 2, 3], sum = 6
Output: true
Explanation: Subset {1, 2, 3} has sum 6.

Constraints:
- 1 <= arr.length <= 100
- 1 <= arr[i] <= 100
- 1 <= sum <= 10^4
"""


def subset(arr, S, N):
    dp = [[False] * (S + 1) for _ in range(N + 1)]

    for n in range(N + 1):
        dp[n][0] = True
    
    for n in range(1, N + 1):
        for s in range(1, S + 1):
            if arr[n - 1] <= s:
                dp[n][s] = dp[n - 1][s - arr[n - 1]] or dp[n - 1][s]
            else:
                dp[n][s] = dp[n - 1][s]
    
    return dp[N][S]
