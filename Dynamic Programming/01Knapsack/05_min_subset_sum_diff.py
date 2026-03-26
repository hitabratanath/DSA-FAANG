"""MINIMUM SUBSET SUM DIFFERENCE

Given an array arr[] of integers, partition the array into two subsets such that the absolute 
difference between the sum of elements in both subsets is minimum and return this minimum difference.

Example 1:
Input: arr = [1, 6, 11, 5]
Output: 1
Explanation: Subset1 = {1, 5, 6}, sum = 12. Subset2 = {11}, sum = 11. Difference = 1.

Example 2:
Input: arr = [1, 4]
Output: 3
Explanation: Subset1 = {1}, sum = 1. Subset2 = {4}, sum = 4. Difference = 3.

Example 3:
Input: arr = [1, 2, 7]
Output: 4
Explanation: Subset1 = {1, 2}, sum = 3. Subset2 = {7}, sum = 7. Difference = 4.

Constraints:
- 1 <= arr.length <= 100
- 1 <= arr[i] <= 100
"""

def min_subset_sum_difference(arr, N):
    S = sum(arr)
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    for n in range(N + 1):
        dp[n][0] = True

    for n in range(1, N + 1):
        for s in range(1, S + 1):
            if arr[n - 1] <= s:
                dp[n][s] = dp[n - 1][s - arr[n - 1]] or dp[n - 1][s]
            else:
                dp[n][s] = dp[n - 1][s]
    
    for s in range(S // 2, -1, -1):
        if dp[N][s]:
            return S - 2 * s


