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
def matrix_chain_multiplication(arr):
    n = len(arr)
    dp = [[-1] * n for _ in range(n)]
    def solve(i, j):
        if i >= j:
            return 0
        if dp[i][j] != -1: return dp[i][j]
        ans = float('inf')
        for k in range(i, j):
            left = solve(i, k)
            right = solve(k + 1, j)
            temp_ans = left + right + arr[i - 1] * arr[k] * arr[j]
            ans = min(temp_ans, ans)
        dp[i][j] = ans
        return dp[i][j]
    
    return solve(1, n - 1)


# -----------------------------------------------------------
# BOOLEAN PARENTHESIZATION / EVALUATE EXPRESSION TO TRUE
# -----------------------------------------------------------
def count_ways_to_evaluate_true(s):
    dp = {}
    def solve(i, j, is_true):
        if i == j:
            if is_true:
                return 1 if s[i] == 'T' else 0
            else:
                return 1 if s[i] == 'F' else 0
        key = (i, j, is_true)
        if key in dp: return dp[key]
        ans = 0
        for k in range(i + 1, j, 2):
            left_true = solve(i, k - 1, True)
            left_false = solve(i, k - 1, False)
            right_true = solve(k + 1, j, True)
            right_false = solve(k + 1, j, False)
            if is_true:
                if s[k] == '&':
                    temp_ans = left_true * right_true
                elif s[k] == '|':
                    temp_ans = left_true * right_false + left_false * right_true + left_true * right_true
                else:
                    temp_ans = left_true * right_false + left_false * right_true
            else:
                if s[k] == '&':
                    temp_ans = left_false * right_false + left_true * right_false + left_false * right_true
                elif s[k] == '|':
                    temp_ans = left_false * right_false
                else:
                    temp_ans = left_true * right_true + left_false * right_false
            ans += temp_ans
        dp[key] = ans
        return ans
    
    return solve(0, len(s) - 1, True)


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
            if solve(x[:k], y[len(y) - k:]) and solve(x[k:], y[:len(y) - k]):
                memo[(x, y)] = True
                return True
            
        memo[(x, y)] = False    
        return False
    
    return solve(a, b)


# -----------------------------------------------------------
# BURST BALLOONS
# -----------------------------------------------------------
def max_coins(nums):
    def solve(i, j):
        if i > j: return 0

        ans = float('-inf')
        for k in range(i, j + 1):
            left = solve(i, k - 1)
            right = solve(k + 1, j)
            temp_ans = nums[i - 1] * nums[k] * nums[j + 1] + left + right
            ans = max(ans, temp_ans)
        return ans
    
    nums = [1] + nums + [1]
    return solve(1, len(nums) - 2)


# -----------------------------------------------------------
# MINIMUM COST TO CUT STICK
# -----------------------------------------------------------
def min_cost(n, cuts):
    def solve(i, j):
        if i > j: return 0

        min_cost = float('inf')
        for k in range(i, j + 1):
            left = solve(i, k - 1)
            right = solve(k + 1, j)
            temp_ans = cuts[j + 1] - cuts[i - 1] + left + right
            min_cost = min(min_cost, temp_ans)
        
        return min_cost
    
    cuts.sort()
    cuts = [0] + cuts + [n]
    return solve(1, len(cuts) - 2)


# -----------------------------------------------------------
# PALINDROME PARTITIONING II
# -----------------------------------------------------------
def min_cut(s):
    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    dp_palindrome = [[-1] * n for _ in range(n)]

    def is_palindrome(n, m):
        if dp_palindrome[n][m] != -1: return dp_palindrome[n][m]
        N, M = n, m
        while n <= m:
            if s[n] != s[m]:
                dp_palindrome[n][m] = False
                return False
            n += 1
            m -= 1
        
        dp_palindrome[N][M] = True
        return True

    def solve(i, j):
        if i >= j: return 0

        if is_palindrome(i, j): return 0

        if dp[i][j] != -1: return dp[i][j]

        ans = float('inf')
        for k in range(i, j):
            left = solve(i, k)
            right = solve(k + 1, j)
            temp_ans = left + right + 1
            ans = min(ans, temp_ans)
        dp[i][j] = ans
        return dp[i][j]
    return solve(0, n - 1)


# -----------------------------------------------------------
# GUESS NUMBER HIGHER OR LOWER II
# -----------------------------------------------------------
def get_money_amount(n):
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    def solve(i, j):
        if i >= j: return 0
        if dp[i][j] != -1: return dp[i][j]
        ans = float('inf')
        for k in range(i, j + 1):
            ans = min(ans, k + max(solve(i, k - 1), solve(k + 1, j)))
        dp[i][j] = ans
        return ans
            
    return solve(1, n)


# -----------------------------------------------------------
# MINIMUM SCORE TRIANGULATION
# -----------------------------------------------------------
def min_score_triangulation(values):
    n = len(values)
    dp = [[-1] * n for _ in range(n)]
    def solve(i, j):
        if j - i < 2: return 0
        if j - i == 2:
            dp[i][j] = values[i] * values[i + 1] * values[j]
            return dp[i][j]

        ans = float('inf')
        for k in range(i + 1, j):
            cost = values[i] * values[k] * values[j]
            left = solve(i, k)
            right = solve(k, j)
            ans = min(ans, cost + left + right)
        
        dp[i][j] = ans
        return ans
    
    return solve(0, n - 1)


# -----------------------------------------------------------
# SPLIT ARRAY LARGEST SUM
# -----------------------------------------------------------
def split_array(nums, p):
    def solve(i, j, p):
        if p == 1: return sum(nums[i: j + 1])

        ans = float('inf')
        for k in range(i, j - p + 2):
            left = sum(nums[i: k + 1])
            right = solve(k + 1, j, p - 1)
            temp_ans = max(left,  right)
            ans = min(ans, temp_ans)
        
        return ans
    
    return solve(0, len(nums) - 1, p)

