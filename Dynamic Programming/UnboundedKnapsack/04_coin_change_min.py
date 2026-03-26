"""COIN CHANGE - MINIMUM COINS

You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money. Return the fewest number of coins that 
you need to make up that amount. If that amount cannot be made up, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1 (3 coins).

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:
Input: coins = [1], amount = 0
Output: 0
Explanation: No coins are needed for amount 0.

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""

def coin_change_min_coins(coins, S, N):
    dp = [[float('inf')] * (S + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 0

    for n in range(1, N + 1):
        for s in range(1, S + 1):
            if coins[n - 1] <= s:
                dp[n][s] = min(1 + dp[n][s - coins[n - 1]], dp[n - 1][s])
            else:
                dp[n][s] = dp[n - 1][s]
    
    return dp[N][S] if dp[N][S] != float('inf') else -1