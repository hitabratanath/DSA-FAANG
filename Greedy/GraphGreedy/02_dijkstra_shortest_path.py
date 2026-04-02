"""DIJKSTRA'S SHORTEST PATH ALGORITHM

Given a graph and a source vertex in the graph, find the shortest paths from the source to all vertices in the given graph.

Example 1:
Input:
V = 2
adj = [[[1, 9]], [[0, 9]]]
S = 0
Output: [0, 9]
Explanation:
Shortest path from 0 to 1 is 0->1 with edge weight 9.

Example 2:
Input:
V = 3, E = 3
adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
S = 2
Output: [4, 3, 0]
Explanation:
For nodes 2 to 0, we can follow the path 2-1-0. This has a distance of 1+3 = 4,
whereas the path 2-0 has a distance of 6. So, the Shortest path from 2 to 0 is 4.
The shortest path from 2 to 1 is 3.
And, the shortest path from 2 to 2 is 0.

Constraints:
- 1 <= V <= 1000
- 0 <= adj[i][j] <= 1000
- 1 <= adj[i].size() <= V
- 0 <= S < V

Time Complexity: O((V + E) log V)
Space Complexity: O(V)
"""

def dijkstra(V, adj, S):
    pass