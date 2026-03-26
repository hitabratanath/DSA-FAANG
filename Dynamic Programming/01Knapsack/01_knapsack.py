"""0/1 KNAPSACK PROBLEM

You are given weights and values of n items, and a knapsack with capacity W. 
You need to maximize the total value in the knapsack. You can either include an item or exclude it (0/1 property).

Example 1:
Input: values = [60, 100, 120], weights = [10, 20, 30], W = 50
Output: 220
Explanation: Take items with values 100 and 120 (weights 20 and 30).

Example 2:
Input: values = [10, 15, 40], weights = [1, 2, 3], W = 6
Output: 65
Explanation: Take all three items.

Example 3:
Input: values = [1, 4, 5, 7], weights = [1, 3, 4, 5], W = 7
Output: 9
Explanation: Take items with values 4 and 5 (weights 3 and 4).

Constraints:
- 1 <= n <= 1000
- 1 <= W <= 1000
- 1 <= weights[i], values[i] <= 1000
"""

def knapsack(value, wt, N, W):
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for w in range(1, W + 1):
            if wt[n - 1] <= w:
                dp[n][w] = max(value[n - 1] + dp[n - 1][w - wt[n - 1]], dp[n - 1][w])
            else:
                dp[n][w] = dp[n - 1][w]
    
    return dp[N][W]
