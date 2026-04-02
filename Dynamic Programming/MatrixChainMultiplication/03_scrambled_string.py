"""SCRAMBLED STRING

We can scramble a string s to get a string t using the following algorithm:
1. If the length of the string is 1, stop.
2. If the length of the string is > 1, do the following:
   - Split the string into two non-empty substrings at a random index.
   - Randomly decide to swap the two substrings or keep them in the same order.
   - Apply this algorithm recursively on each substring.

Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise return false.

Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scrambling: "great" -> "gr/eat" -> "gr/eat" -> "rg/eat" -> "rge/at" -> "rgeat"

Example 2:
Input: s1 = "abcdef", s2 = "fecabd"
Output: true

Example 3:
Input: s1 = "a", s2 = "a"
Output: true

Example 4:
Input: s1 = "hwareg", s2 = "grhwae"
Output: false

Constraints:
- s1.length == s2.length
- 1 <= s1.length <= 30
- s1 and s2 consist of lowercase English letters.
"""

def scramble_string(a, b):
    if len(a) != len(b): return False
    if sorted(a) != sorted(b): return False
    if a == b: return True

    def solve(x, y):
        if len(x) == 1:
            return x == y
        
        if x == y:
            return True
        
        for k in range(1, len(x)):
            # without swap
            if solve(x[: k], y[: k]) and solve(x[k:], y[k:]):
                return True
            
            # with swap
            if solve(x[: k], y[len(y) - k: ]) and solve(x[k:], y[: len(y) - k]):
                return True
            
        return False
                

    return solve(a, b) 