"""PRINT SHORTEST COMMON SUPERSEQUENCE

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.
If there are multiple valid strings, return any of them.

A string s is a supersequence of strings str1 and str2 if both str1 and str2 are subsequences of s.

Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: "cabac" is the shortest supersequence. Other valid answers include "abcab" or "acbac".

Example 2:
Input: str1 = "geek", str2 = "eke"
Output: "geeke"
Explanation: "geeke" is one possible shortest supersequence.

Example 3:
Input: str1 = "abc", str2 = "def"
Output: "abcdef"
Explanation: The shortest supersequence is "abcdef" or "defabc".

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of only lowercase English characters.
"""

def print_shortest_common_supersequence(a, b):
    N, M = len(a), len(b)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if a[n - 1] == b[m - 1]:
                dp[n][m] = 1 + dp[n - 1][m - 1]
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])
    
    n, m = N, M
    scs = []
    while n > 0 and m > 0:
        if a[n - 1] == b[m - 1]:
            scs.append(a[n - 1])
            n -= 1
            m -= 1
        elif dp[n - 1][m] > dp[n][m - 1]:
            scs.append(a[n - 1])
            n -= 1
        else:
            scs.append(b[m - 1])
            m -= 1
    
    while n > 0:
        scs.append(a[n - 1])
        n -= 1
    while m > 0:
        scs.append(b[m - 1])
        m -= 1
    
    return "".join(reversed(scs))
