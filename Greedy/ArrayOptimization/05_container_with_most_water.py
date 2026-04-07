"""CONTAINER WITH MOST WATER

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Time Complexity: O(n)
Space Complexity: O(1)
"""

'''
Key Insight - Elimination Argument:

When you have pointers at positions i and j where height[i] < height[j], and you move the left pointer from i to i+1, you're effectively eliminating ALL containers of the form (i, k) where i < k < j.

Why can we safely eliminate these?

Any container (i, k) has area = min(height[i], height[k]) × (k - i)

Since height[i] is the bottleneck, the area is at most height[i] × (k - i)

But (k - i) < (j - i), so area of (i, k) < area of (i, j)

We've already considered (i, j), so (i, k) can never be better
'''

def max_area(height):
    pass