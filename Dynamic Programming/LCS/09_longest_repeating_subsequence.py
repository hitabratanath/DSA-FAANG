"""LONGEST REPEATING SUBSEQUENCE

Given a string s, return the length of the longest repeating subsequence such that the two subsequences 
don't have the same character at the same position, i.e., any ith character in the two subsequences 
shouldn't have the same index in the original string.

Example 1:
Input: s = "aabebcdd"
Output: 3
Explanation: The longest repeating subsequence is "abd" (indices 0,2,5 and 1,3,6).

Example 2:
Input: s = "abc"
Output: 0
Explanation: There is no repeating subsequence.

Example 3:
Input: s = "aab"
Output: 1
Explanation: The longest repeating subsequence is "a".

Example 4:
Input: s = "axxxy"
Output: 2
Explanation: The longest repeating subsequence is "xx".

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.
"""

def longest_repeating_subsequence(a):
    N = len(a)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for m in range(1, N + 1):
            if a[n - 1] == a[m - 1] and n != m:
                dp[n][m] = 1 + dp[n - 1][m - 1]
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])
    
    return dp[N][N]
