"""OPTIMAL BINARY SEARCH TREE

Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the number of searches to keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.

Let us first define the cost of a BST. The cost of a BST node is level of that node multiplied by its frequency. Level of root is 1.

Example 1:
Input: keys = [10, 12], freq = [34, 50]
Output: 118
Explanation: There can be following two possible BSTs 
        10                12
          \             /
           12         10
          I         II
Frequency of searches of 10 and 12 are 34 and 50 respectively.
The cost of tree I is 34*1 + 50*2 = 134
The cost of tree II is 50*1 + 34*2 = 118

Example 2:
Input: keys = [10, 12, 20], freq = [34, 8, 50]
Output: 142
Explanation: There can be following possible BSTs, we need to return the minimum cost BST.

Constraints:
- 1 <= n <= 100
- All keys are distinct
- freq[i] >= 1
"""

def optimal_search_tree(keys, freq, n):
    pass