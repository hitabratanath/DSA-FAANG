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
    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True
    
    def solve(i, j):
        if i >= j: return 0
        if is_palindrome(i, j):
            return 0

        ans = float('inf')
        for k in range(i, j):
            ans = min(ans, 1 + solve(i, k) + solve(k + 1, j))
        return ans
    
    return solve(0, len(s) - 1)