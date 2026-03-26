"""COIN CHANGE - MAXIMUM WAYS

You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money. Return the number of combinations that 
make up that amount. You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: There are four ways: 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1.

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1
Explanation: Only one way: 10=10.

Constraints:
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- 0 <= amount <= 5000
"""

def coin_change_max_ways(coins, S, N):
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    
    for n in range(1, N + 1):
        for s in range(1, S + 1):
            if coins[n - 1] <= s:
                dp[n][s] = dp[n][s - coins[n - 1]] + dp[n - 1][s]
            else:
                dp[n][s] = dp[n - 1][s]
    
    return dp[N][S]
