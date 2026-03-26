"""LONGEST COMMON SUBSTRING

Given two strings text1 and text2, return the length of their longest common substring.
If there is no common substring, return 0.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: text1 = "abcde", text2 = "abfce"
Output: 2
Explanation: The longest common substring is "ab" and its length is 2.

Example 2:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common substring.

Example 3:
Input: text1 = "abcdef", text2 = "zabcf"
Output: 3
Explanation: The longest common substring is "abc" and its length is 3.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
"""

def longest_common_substring(a, b):
    N, M = len(a), len(b)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    result = 0

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if a[n - 1] == b[m - 1]:
                dp[n][m] = 1 + dp[n - 1][m - 1]
                result = max(result, dp[n][m])
            else:
                dp[n][m] = 0
    
    return result
