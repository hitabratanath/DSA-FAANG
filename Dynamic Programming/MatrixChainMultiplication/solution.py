# -----------------------------------------------------------
# GENERAL FORMAT
# -----------------------------------------------------------

# def solve(arr, i, j):
#     if base_condition:
#         return base_condition_value

#     for k in range(i, j):
#         left = solve(i, k)
#         right = solve(k + 1, j)
#         temp_ans = left + right + some_cost_operation(arr, i, k, j)

#         ans = select_ans(ans, temp_ans)
    
#     return ans


# -----------------------------------------------------------
# MATRIX CHAIN MULTIPLICATION
# -----------------------------------------------------------  
def mcm(arr, i, j):
    if i >= j:
        return 0
    
    ans = float('inf')
    for k in range(i, j):
        left = mcm(arr, i, k)
        right = mcm(arr, k + 1, j)
        temp_ans = left + right + arr[i - 1] * arr[k] * arr[j]
        ans = min(ans, temp_ans)

    return ans

# -----------------------------------------------------------
# MATRIX CHAIN MULTIPLICATION MEMOIZATION
# -----------------------------------------------------------  
# dp = [[-1] * n for _ in range(n)]
def mcm_memoization(arr, i, j, dp):
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    ans = float('inf')
    for k in range(i, j):
        left = mcm_memoization(arr, i, k, dp)
        right = mcm_memoization(arr, k + 1, j, dp)
        temp_ans = left + right + arr[i - 1] * arr[k] * arr[j]
        ans = min(temp_ans, ans)
    dp[i][j] = ans
    return ans


# -----------------------------------------------------------
# PALINDROME PARTITIONING
# -----------------------------------------------------------  
def is_palindrome(s, i, j):
    pass

def palindrome_partitioning(s, i, j):
    pass


# -----------------------------------------------------------
# PALINDROME PARTITIONING - MEMOIZATION
# -----------------------------------------------------------
def palindrome_partitioning_memo(s, i, j, dp):
    pass


# -----------------------------------------------------------
# BOOLEAN PARENTHESIZATION / EVALUATE EXPRESSION TO TRUE
# -----------------------------------------------------------
def count_evalutate_expression(s, i, j, is_true):
    pass


# -----------------------------------------------------------
# SCRAMBLED STRING
# -----------------------------------------------------------
def scramble_string(a, b):
    if a == b: return True
    if sorted(a) != sorted(b): return False
    if len(a) != len(b): return False

    memo = {}
    def solve(x, y):
        if (x, y) in memo: return memo[(x, y)]
        if len(x) == 1:
            memo[(x, y)] =  x == y
            return memo[(x, y)]
        
        if x == y:
            memo[(x, y)] = True
            return True

        for k in range(1, len(x)):
            # without swap
            if solve(x[:k], y[:k]) and solve(x[k:], y[k:]):
                memo[(x, y)] = True
                return True
            
            # with swap
            if solve(x[:k], y[len(y) - k:] and solve(x[:k], y[:len(y) - k])):
                memo[(x, y)] = True
                return True
            
        memo[(x, y)] = False    
        return False
    
    return solve(a, b)


# -----------------------------------------------------------
# BURST BALLOONS
# -----------------------------------------------------------
def max_coins(nums):
    pass


# -----------------------------------------------------------
# MINIMUM COST TO CUT STICK
# -----------------------------------------------------------
def min_cost(n, cuts):
    pass


# -----------------------------------------------------------
# PALINDROME PARTITIONING II
# -----------------------------------------------------------
def min_cut(s):
    pass


# -----------------------------------------------------------
# GUESS NUMBER HIGHER OR LOWER II
# -----------------------------------------------------------
def get_money_amount(n):
    pass


# -----------------------------------------------------------
# MINIMUM SCORE TRIANGULATION
# -----------------------------------------------------------
def min_score_triangulation(values):
    pass


# -----------------------------------------------------------
# SPLIT ARRAY LARGEST SUM
# -----------------------------------------------------------
def split_array(nums, k):
    pass

