"""PALINDROME PARTITIONING II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "raceacar"
Output: 0
Explanation: s is already a palindrome, hence requires no cuts.

Example 3:
Input: s = "abcde"
Output: 4
Explanation: The minimum cuts needed are 4. One possible way is to cut as ["a","b","c","d","e"].

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters only.

Note: This is the same as problem 02_palindrome_partitioning.py but included separately as it's frequently asked as "Palindrome Partitioning II" in interviews.
"""

def min_cut(s):
    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    dp_palindrome = [[-1] * n for _ in range(n)]

    def is_palindrome(n, m):
        if dp_palindrome[n][m] != -1: return dp_palindrome[n][m]
        N, M = n, m
        while n <= m:
            if s[n] != s[m]:
                dp_palindrome[n][m] = False
                return False
            n += 1
            m -= 1
        
        dp_palindrome[N][M] = True
        return True

    def solve(i, j):
        if i >= j: return 0

        if is_palindrome(i, j): return 0

        if dp[i][j] != -1: return dp[i][j]

        ans = float('inf')
        for k in range(i, j):
            left = solve(i, k)
            right = solve(k + 1, j)
            temp_ans = left + right + 1
            ans = min(ans, temp_ans)
        dp[i][j] = ans
        return dp[i][j]
    return solve(0, n - 1)