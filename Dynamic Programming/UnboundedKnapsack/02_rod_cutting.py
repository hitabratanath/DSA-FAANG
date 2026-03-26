"""ROD CUTTING PROBLEM

Given a rod of length L and arrays of available piece lengths and their corresponding prices,
determine the maximum value obtainable by cutting up the rod and selling the pieces.
You can use the same piece length multiple times.

Example 1:
Input: length = [1, 2, 3, 4, 5, 6, 7, 8], price = [1, 5, 8, 9, 10, 17, 17, 20], L = 8, n = 8
Output: 22
Explanation: Cut the rod into pieces of length 2 and 6 (price = 5 + 17 = 22).

Example 2:
Input: length = [1, 2, 3, 4], price = [2, 5, 7, 8], L = 5, n = 4
Output: 12
Explanation: Cut into pieces of length 2 and 3 (price = 5 + 7 = 12).

Example 3:
Input: length = [1, 2, 3, 4, 5], price = [2, 5, 7, 8, 10], L = 5, n = 5
Output: 12
Explanation: Cut into pieces of length 2 and 3 (price = 5 + 7 = 12).

Constraints:
- 1 <= L <= 1000 (rod length)
- 1 <= n <= 1000 (number of available piece lengths)
- 1 <= price[i] <= 10^6
"""

def rod_cutting(length, price, L, N):
    dp = [[0] * (L + 1) for _ in range(N + 1)]

    for l in range(1, N + 1):
        for n in range(1, L + 1):
            if length[n - 1] <= l:
                dp[n][l] = max(price[n - 1] + dp[n][l - length[n - 1]], dp[n - 1][l])
            else:
                dp[n][l] = dp[n - 1][l]
    
    return dp[N][L]
