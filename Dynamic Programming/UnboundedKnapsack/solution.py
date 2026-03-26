# -----------------------------------------------------------
# GENERAL UNBOUNDED KNAPSACK
# -----------------------------------------------------------
def unbounded_knapsack(value, wt, W, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(value[i - 1] + dp[i][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]


# -----------------------------------------------------------
# ROD CUTTING
# -----------------------------------------------------------
def rod_cutting(length, price, L, n):
    dp = [[0] * (L + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for l in range(1, L + 1):
            if length[i - 1] <= l:
                dp[i][l] = max(price[i - 1] + dp[i][l - length[i - 1]], dp[i - 1][l])
            else:
                dp[i][l] = dp[i - 1][l]
    
    return dp[n][L]


# -----------------------------------------------------------
# COIN CHANGE MAX WAYS
# -----------------------------------------------------------
def coin_change_max_ways(coins, S, n):
    dp = [[0] * (S + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    

    for i in range(1, n + 1):
        for s in range(1, S + 1):
            if coins[i - 1] <= s:
                dp[i][s] = dp[i][s - coins[i - 1]] + dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    return dp[n][S]


# -----------------------------------------------------------
# COIN CHANGE MIN COINS
# -----------------------------------------------------------
def coin_change_min_coins(coins, S, n):
    dp = [[float('inf')] * (S + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    
    for i in range(1, n + 1):
        for s in range(1, S + 1):
            if coins[i - 1] <= s:
                dp[i][s] = min(1 + dp[i][s - coins[i - 1]], dp[i - 1][s])
            else:
                dp[i][s] = dp[i - 1][s]
    
    return dp[n][S] if dp[n][S] != float('inf') else -1
