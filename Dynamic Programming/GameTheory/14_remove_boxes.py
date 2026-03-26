"""REMOVE BOXES (LeetCode 546)

You are given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there are no boxes left.
Each time you can choose some continuous boxes with the same color (composed of k boxes), 
remove them and get k * k points.

Return the maximum points you can get.

Example 1:
Input: boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
Output: 23
Explanation: 
[1, 3, 2, 2, 2, 3, 4, 3, 1] -> [1, 3, 3, 4, 3, 1] (3*3=9) -> [1, 3, 3, 3, 1] (1*1=1) 
-> [1, 1] (3*3=9) -> [] (2*2=4). Total = 23.

Example 2:
Input: boxes = [1, 1, 1]
Output: 9

Example 3:
Input: boxes = [1]
Output: 1

Constraints:
- 1 <= boxes.length <= 100
- 1 <= boxes[i] <= 100
"""

def remove_boxes(boxes):
    pass
