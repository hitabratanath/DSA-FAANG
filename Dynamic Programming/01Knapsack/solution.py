# -----------------------------------------------------------
# GENERAL IMPLEMENTATION - MEMOIZATION
# -----------------------------------------------------------
def knapsackMemo(value, wt, n, W, memo={}):
    if (n, W) in memo:
        return memo[(n, W)]
    
    if n < 0 or W == 0:
        return 0
    
    if wt[n] <= W:
        include = value[n] + knapsackMemo(value, wt, n - 1, W - wt[n], memo)
        exclude = knapsackMemo(value, wt, n - 1, W, memo)
        result = max(include, exclude)
    else:
        result = knapsackMemo(value, wt, n - 1, W, memo)
    
    memo[(n, W)] = result
    return result


# -----------------------------------------------------------
# GENERAL IMPLEMENTATION - TABULATION
# -----------------------------------------------------------
def knapsack(value, wt, N, W):
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for w in range(1, W + 1):
            if wt[n - 1] <= w:
                dp[n][w] = max(value[n - 1] + dp[n - 1][w - wt[n - 1]], dp[n - 1][w])
            else:
                dp[n][w] = dp[n - 1][w]
    
    return dp[N][W]


# -----------------------------------------------------------
# SUBSET EXISTS
# -----------------------------------------------------------
def subset(arr, sm, n):
    dp = [[False] * (sm + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in  range(1, n + 1):
        for s in range(1, sm + 1):
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i - 1]] or dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    return dp[n][sm]


# -----------------------------------------------------------
# EQUAL SUM PARTITION
# -----------------------------------------------------------
def equal_sum_partition(arr, n):
    total = sum(arr)
    if total % 2 != 0: return False

    sm = total // 2

    dp = [[False] * (sm + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for s in range(1, sm + 1):
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i - 1]] or dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    return dp[n][sm]


# -----------------------------------------------------------
# COUNT SUBSET WITH GIVEN SUM
# -----------------------------------------------------------
def count_subset_given_sum(arr, sm, n):
    dp = [[0] * (sm + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for s in range(1, sm + 1):
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i - 1]] + dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    return dp[n][sm]


# -----------------------------------------------------------
# MINIMUM SUBSET SUM DIFFERENCE
# -----------------------------------------------------------
def min_subset_sum_difference(arr, n):
    sm = sum(arr)

    dp = [[False] * (sm + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for s in range(1, sm + 1):
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i - 1]] or dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    ans = sm
    for s in range(sm // 2 + 1, -1, -1):
        if dp[n][s]:
            ans = sm - 2 * s
            break
    
    return ans


# -----------------------------------------------------------
# COUNT SUBSET WITH GIVEN DIFFERENCE
# -----------------------------------------------------------
def count_subset_given_diff(arr, d, n):
    sm = sum(arr)
    if (sm + d) % 2 != 0: return 0
    target = (sm + d) // 2

    dp = [[0] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for s in range(1, target + 1):
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i - 1]] + dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    return dp[n][target]


# -----------------------------------------------------------
# TARGET SUM
# -----------------------------------------------------------
def target_sum(arr, sm, n):
    total = sum(arr)
    if (total + sm) % 2 != 0: return 0
    target = (total + sm) // 2

    if target < 0: return 0
    
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for s in range(1, target + 1):
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i - 1]] + dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    return dp[n][target]
