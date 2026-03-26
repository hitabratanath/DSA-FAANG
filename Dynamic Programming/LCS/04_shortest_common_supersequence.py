"""SHORTEST COMMON SUPERSEQUENCE

Given two strings str1 and str2, return the length of the shortest string that has both str1 and str2 as subsequences.
If there are multiple valid strings, return the length of any of them.

A string s is a supersequence of strings str1 and str2 if both str1 and str2 are subsequences of s.

Example 1:
Input: str1 = "abac", str2 = "cab"
Output: 5
Explanation: One possible shortest supersequence is "cabac" with length 5.

Example 2:
Input: str1 = "geek", str2 = "eke"
Output: 5
Explanation: One possible shortest supersequence is "geeke" with length 5.

Example 3:
Input: str1 = "abc", str2 = "def"
Output: 6
Explanation: The shortest supersequence is "abcdef" with length 6.

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of only lowercase English characters.
"""

# N - lcs = extra1
# M - lcs = extra2
# N - lcs + M
# N + M - lcs

def shortest_common_supersequence(a, b):
    N, M = len(a), len(b)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if a[n - 1] == b[m - 1]:
                dp[n][m] = 1 + dp[n- 1][m - 1]
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])
    
    return N + M - dp[N][M]
