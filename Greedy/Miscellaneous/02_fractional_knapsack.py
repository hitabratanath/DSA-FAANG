"""FRACTIONAL KNAPSACK

Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In Fractional Knapsack, we can break items for maximizing the total value of knapsack.

Example 1:
Input: n = 3, W = 50
values[] = {60, 100, 120}
weights[] = {10, 20, 30}
Output: 240.00
Explanation: Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20 = 80, so the total value becomes 60+100+80.0 = 240.0

Example 2:
Input: n = 2, W = 50
values[] = {60, 100}
weights[] = {10, 20}
Output: 160.00
Explanation: Take both items completely, so the total value becomes 60+100 = 160.0

Constraints:
- 1 <= n <= 10^5
- 1 <= W <= 10^9
- 1 <= values[i], weights[i] <= 10^4

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def fractional_knapsack(W, arr, n):
    pass