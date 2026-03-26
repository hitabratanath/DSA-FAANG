"""PRINTING LONGEST COMMON SUBSEQUENCE

Given two strings text1 and text2, return the longest common subsequence as a string.
If there is no common subsequence, return an empty string.
If there are multiple solutions, return any of them.

A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: "ace"
Explanation: The longest common subsequence is "ace".

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: "abc"
Explanation: The longest common subsequence is "abc".

Example 3:
Input: text1 = "abc", text2 = "def"
Output: ""
Explanation: There is no such common subsequence.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
"""

def printing_longest_common_subsequence(a, b):
    N, M = len(a), len(b)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if a[n - 1] == b[m - 1]:
                dp[n][m] = 1 + dp[n - 1][m - 1]
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])

    lcs = []
    n, m = N, M
    while n > 0 and m > 0:
        if a[n - 1] == b[m - 1]:
            lcs.append(a[n - 1])
            n -= 1
            m -= 1
        elif dp[n][m - 1] > dp[n - 1][m]:
            m -= 1
        else:
            n -= 1
    
    return ''.join(reversed(lcs))
