"""MINIMUM INSERTION AND DELETION

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string or insert one character.
Return [insertions, deletions] where insertions is the number of insertions needed and deletions is the number of deletions needed.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: [1, 1]
Explanation: You need 1 deletion from word1 ("s") and 1 insertion to word1 ("t").

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: [0, 4]
Explanation: You need 4 deletions from word1 to make it "etco".

Example 3:
Input: word1 = "abc", word2 = "abc"
Output: [0, 0]
Explanation: Both strings are already the same.

Constraints:
- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English characters.
"""

# N - lcs = extra1 = deletion
# M - lcs = extra2 = insertion
# ans = [M - lcs, N - lcs]

def min_insertion_deletion(a, b):
    N, M = len(a), len(b)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if a[n - 1] == b[m - 1]:
                dp[n][m] = 1 + dp[n - 1][m - 1]
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])
    
    return [M - dp[N][M], N - dp[N][M]]
