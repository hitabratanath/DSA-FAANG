# -----------------------------------------------------------
# LONGEST COMMON SUBSEQUENCE
# -----------------------------------------------------------
def longest_common_subsequence(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]


# -----------------------------------------------------------
# LONGEST COMMON SUBSTRING
# -----------------------------------------------------------
def longest_common_substring(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_length = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    
    return max_length


# -----------------------------------------------------------
# PRINTING LONGEST COMMON SUBSTRING
# -----------------------------------------------------------
def printing_longest_common_subsequence(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    
    i, j = n, m
    lcs = []
    
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return "".join(reversed(lcs))


# -----------------------------------------------------------
# SHORTEST COMMON SUPER SEQUENCE
# -----------------------------------------------------------
def shortest_common_supersequence(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    
    return n + m - dp[n][m]


# -----------------------------------------------------------
# MIN INSERTION AND DELETION
# -----------------------------------------------------------
def min_insertion_deletion(a, b):
    n, m = len(a), len(b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    lcs_length = dp[n][m]

    deletion = n - lcs_length
    insertion = m - lcs_length

    return [insertion, deletion]


# -----------------------------------------------------------
# LONGEST PALINDROMIC SUBSEQUENCE
# -----------------------------------------------------------
def longest_palindromic_subsequence(a):
    n = len(a)
    # b = a[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1] == a[n - j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][n]


# -----------------------------------------------------------
# MIN DELETION TO MAKE PALINDROME
# -----------------------------------------------------------
def min_deletion_palindrome(a):
    n = len(a)
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1] == a[n - j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return n - dp[n][n]


# -----------------------------------------------------------
# PRINT SHORTEST COMMON SUPERSEQUENCE
# -----------------------------------------------------------
def print_shortest_common_supersequence(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    i, j = n, m
    scs = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            scs.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j - 1] > dp[i - 1][j]:
            scs.append(b[j - 1])
            j -= 1
        else:
            scs.append(a[i - 1])
            i -= 1
    while i > 0:
        scs.append(a[i - 1])
        i -= 1
    
    while j > 0:
        scs.append(b[j - 1])
        j -= 1
            
    return "".join(reversed(scs))


# -----------------------------------------------------------
# LONGEST REPEATING SUBSEQUENCE
# -----------------------------------------------------------
def longest_repeating_subsequence(a):
    n = len(a)

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1] == a[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][n]


# -----------------------------------------------------------
# SUBSEQUENCE PATTERN MATCHING
# -----------------------------------------------------------
def subsequence_pattern_matching(a, b):
    n, m = len(a), len(b)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return n == dp[n][m]


# -----------------------------------------------------------
# MINIMUM INSERTION TO MAKE PALINDROME
# -----------------------------------------------------------
def min_insertion_palindrome(a):
    n = len(a)

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1] == a[n - j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return n - dp[n][n]
