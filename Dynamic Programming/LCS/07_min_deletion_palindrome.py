"""MINIMUM DELETION TO MAKE PALINDROME

Given a string s, return the minimum number of deletions needed to make s a palindrome.

Example 1:
Input: s = "abcda"
Output: 2
Explanation: Remove "b" and "c" to get "ada" which is a palindrome.

Example 2:
Input: s = "aba"
Output: 0
Explanation: The string is already a palindrome.

Example 3:
Input: s = "geek"
Output: 2
Explanation: Remove "g" and "k" to get "ee" which is a palindrome.

Example 4:
Input: s = "abc"
Output: 2
Explanation: Remove "b" and "c" to get "a" which is a palindrome.

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.
"""

def min_deletion_palindrome(a):
    N = len(a)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for m in range(1, N + 1):
            if a[n - 1] == a[N - m]:
                dp[n][m] = 1 + dp[n - 1][m - 1]
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])
    
    return N - dp[N][N]
