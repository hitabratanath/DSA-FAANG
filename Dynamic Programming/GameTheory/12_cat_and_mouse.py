"""CAT AND MOUSE (LeetCode 913)

A game on an undirected graph. Mouse starts at node 1, Cat starts at node 2. 
There is a Hole at node 0. They take turns, Mouse moves first.
On each turn, they must move to an adjacent node. Cat cannot move to the Hole (node 0).

If Cat and Mouse occupy the same node, Cat wins. If Mouse reaches the Hole, Mouse wins.
If a position is repeated, the game is a draw.

Return 1 if Mouse wins, 2 if Cat wins, 0 if draw.

Example 1:
Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0

Example 2:
Input: graph = [[1,3],[0],[3],[0,2]]
Output: 1

Constraints:
- 3 <= graph.length <= 50
- 1 <= graph[i].length < graph.length
- 0 <= graph[i][j] < graph.length
- graph[i][j] != i
- graph[i] is unique
"""

def cat_mouse_game(graph):
    pass
