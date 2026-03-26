"""MINIMUM INSERTION TO MAKE PALINDROME

Given a string s, return the minimum number of insertions needed to make s a palindrome.
You can insert any character at any position of the string.

Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string is already a palindrome.

Example 2:
Input: s = "mbadm"
Output: 2
Explanation: Insert "m" at the beginning and "b" at the end to get "mbdadbm" which is a palindrome.

Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Insert 5 characters to make it a palindrome.

Example 4:
Input: s = "abc"
Output: 2
Explanation: Insert "c" and "b" to get "abcba" which is a palindrome.

Constraints:
- 1 <= s.length <= 500
- s consists only of lowercase English letters.
"""

def min_insertion_palindrome(a):
    N = len(a)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for m in range(1, N + 1):
            if a[n - 1] == a[N - m]:
                dp[n][m] = 1 + dp[n - 1][m - 1]
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])
    
    return N - dp[N][N]
