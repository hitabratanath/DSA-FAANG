"""NUMBER OF DISTINCT SUBSTRINGS IN A STRING

Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters.

Alternatively: Given a string, find the number of distinct substrings of the string.

Example 1:
Input: s = "ababa"
Output: 10
Explanation: All distinct substrings are: "a", "b", "ab", "ba", "aba", "bab", "abab", "baba", "ababa", "babab"
Wait, let me recalculate: "a", "b", "ab", "ba", "aba", "bab", "abab", "baba", "ababa" = 9 distinct substrings

Example 2:
Input: s = "abc"
Output: 6
Explanation: All distinct substrings are: "a", "b", "c", "ab", "bc", "abc"

Example 3:
Input: s = "aaa"
Output: 3
Explanation: All distinct substrings are: "a", "aa", "aaa"

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

Time Complexity: O(N^2) where N is the length of string
Space Complexity: O(N^2) for the trie in worst case
"""

def countDistinctSubstrings(s):
    pass