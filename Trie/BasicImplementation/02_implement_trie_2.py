"""IMPLEMENT TRIE-2 (WITH COUNT FUNCTIONS)

Implement a trie with additional functionality to count words and prefixes.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
- int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
- void erase(String word) Erases the string word from the trie.

Example 1:
Input: ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo"]
       [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"]]
Output: [null, null, null, 2, 2, null, 1]

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase.
- It is guaranteed that for any function call to erase, the string word will exist in the trie.

Time Complexity: O(m) for all operations, where m is the key length
Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of keys and M is average key length
"""

class Trie:
    def __init__(self):
        pass
    
    def insert(self, word: str) -> None:
        pass
    
    def countWordsEqualTo(self, word: str) -> int:
        pass
    
    def countWordsStartingWith(self, prefix: str) -> int:
        pass
    
    def erase(self, word: str) -> None:
        pass