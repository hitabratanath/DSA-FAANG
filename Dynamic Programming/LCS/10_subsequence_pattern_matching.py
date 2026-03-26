"""SUBSEQUENCE PATTERN MATCHING

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters.

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Explanation: "abc" is a subsequence of "ahbgdc".

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
Explanation: "axc" is not a subsequence of "ahbgdc".

Example 3:
Input: s = "ace", t = "abcde"
Output: true
Explanation: "ace" is a subsequence of "abcde".

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.
"""

def subsequence_pattern_matching(a, b):
    N, M = len(a), len(b)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if a[n - 1] == b[m - 1]:
                dp[n][m] = 1 + dp[n - 1][m - 1]
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])
    
    return dp[N][M] == N
