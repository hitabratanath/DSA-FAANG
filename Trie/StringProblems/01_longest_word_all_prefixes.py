"""LONGEST WORD WITH ALL PREFIXES (COMPLETE STRING)

Given an array of strings words, find the longest string in words such that every prefix of it is also in words.

For example, let words = ["w", "wo", "wor", "worl", "world"]. The word "world" is the longest word in words that can be built one character at a time by other words in words.

Return the longest word in words that can be built one character at a time by other words in words. If there are more than one possible answers, return the lexicographically smallest one among them.

Example 1:
Input: words = ["w", "wo", "wor", "worl", "world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 30
- words[i] consists of lowercase English letters.

Time Complexity: O(N * M) where N is number of words and M is average word length
Space Complexity: O(N * M) for the trie
"""

def longestWord(words):
    pass