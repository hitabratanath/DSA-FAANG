"""STONE GAME II (LeetCode 1140)

Alice and Bob take turns playing a game, with Alice starting first.
There are n piles of stones arranged in a row. On each player's turn, they can take all stones 
from the first X remaining piles, where 1 <= X <= 2M. Then M = max(M, X).
Initially M = 1. The game ends when all piles are taken.

Return the maximum number of stones Alice can get.

Example 1:
Input: piles = [2, 7, 9, 4, 4]
Output: 10
Explanation: Alice takes 1 pile (2), M=1. Bob takes 2 piles (7,9), M=2. 
Alice takes 2 piles (4,4). Alice = 10.

Example 2:
Input: piles = [1, 2, 3, 4, 5, 100]
Output: 104

Constraints:
- 1 <= piles.length <= 100
- 1 <= piles[i] <= 10^4
"""

def stone_game_ii(piles):
    pass
