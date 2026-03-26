"""UNBOUNDED KNAPSACK

Given a knapsack weight W and a set of n items with certain value and weight, we need to 
calculate the maximum value that can be accommodated in the knapsack. Unlike 0/1 knapsack, 
you are allowed to use unlimited number of instances of an item.

Example 1:
Input: W = 100, values = [10, 30, 20], weights = [5, 10, 15]
Output: 300
Explanation: Take 10 items of value 30 each (weight 10 each).

Example 2:
Input: W = 8, values = [1, 4, 5, 7], weights = [1, 3, 4, 5]
Output: 11
Explanation: Take 2 items of value 4 (weight 3 each) and 1 item of value 1 (weight 1).

Example 3:
Input: W = 10, values = [5, 11, 13], weights = [2, 4, 6]
Output: 27
Explanation: Take 2 items of value 13 (weight 6) and 1 item of value 5 (weight 2).

Constraints:
- 1 <= n <= 1000
- 1 <= W <= 1000
- 1 <= weights[i], values[i] <= 1000
"""

def unbounded_knapsack(value, wt, W, N):
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for w in range(1, W + 1):
            if wt[n - 1] <= w:
                dp[n][w] = max(dp[n][w - wt[n - 1]] + value[n - 1], dp[n - 1][w])
            else:
                dp[n][w] = dp[n - 1][w]
    
    return dp[N][W]


from functools import lru_cache
def unbounded_knapsack_memo(value, wt, W, N):

    @lru_cache(None)
    def helper(n, w):
        if n == 0 or w == 0:
            return 0
        if wt[n - 1] <= w:
            return max(value[n - 1] + helper(n, w - wt[n - 1]), helper(n - 1, w))
        else:
            return helper(n - 1, w)
    
    return helper(N, W)
