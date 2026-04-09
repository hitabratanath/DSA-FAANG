"""IMPLEMENT TRIE (PREFIX TREE)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
       [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output: [null, null, true, false, true, null, true]

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Time Complexity: O(m) for all operations, where m is the key length
Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of keys and M is average key length
"""

class Trie:
    def __init__(self):
        pass
    
    def insert(self, word: str) -> None:
        pass
    
    def search(self, word: str) -> bool:
        pass
    
    def startsWith(self, prefix: str) -> bool:
        pass