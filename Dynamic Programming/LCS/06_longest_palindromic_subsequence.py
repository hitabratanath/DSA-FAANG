"""LONGEST PALINDROMIC SUBSEQUENCE

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements 
without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Example 3:
Input: s = "a"
Output: 1
Explanation: The longest palindromic subsequence is "a".

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.
"""

def longest_palindromic_subsequence(a):
    N = len(a)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for m in range(1, N + 1):
            if a[n - 1] == a[N - m]:
                dp[n][m] = 1 + dp[n - 1][m - 1]
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])
    
    return dp[N][N]
