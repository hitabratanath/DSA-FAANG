"""CAT AND MOUSE II (LeetCode 1728)

A game is played on a grid. Mouse and Cat take turns, Mouse moves first.
Mouse starts at 'M', Cat starts at 'C', and there is a food cell 'F'.
Mouse can jump at most mouseJump cells, Cat can jump at most catJump cells (horizontal or vertical).
They cannot jump over walls ('#'). Mouse wins if it reaches food first. Cat wins if it catches 
Mouse or reaches food first. If 1000 turns pass, Cat wins.

Return true if Mouse can win.

Example 1:
Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
Output: True

Example 2:
Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
Output: True

Example 3:
Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
Output: False

Constraints:
- 1 <= rows, cols <= 8
- grid[i][j] is one of '.', '#', 'C', 'M', 'F'
- 1 <= catJump, mouseJump <= 8
"""

def can_mouse_win(grid, catJump, mouseJump):
    pass
