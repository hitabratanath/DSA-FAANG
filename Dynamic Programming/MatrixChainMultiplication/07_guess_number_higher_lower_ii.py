"""GUESS NUMBER HIGHER OR LOWER II

We are playing the Guessing Game. The game will work as follows:

1. I pick a number between 1 and n.
2. You guess a number.
3. If you guess the wrong number, I will tell you whether the number I picked is higher or lower than your guess.
4. Every time you guess a wrong number x, you will pay x dollars.

Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.

Example 1:
Input: n = 10
Output: 16
Explanation: The winning strategy is:
- Start with 7.
  - If this is my number, your total is $0. Otherwise, you pay $7.
  - If my number is higher, it costs $7 + $9 = $16. If my number is lower, it costs $7 + $4 = $11.
- So you must have $16 to guarantee a win.

Example 2:
Input: n = 1
Output: 0
Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.

Example 3:
Input: n = 2
Output: 1
Explanation: There are two possible numbers, 1 and 2.
- Guess 1, pay $0, and get the answer.
- If the answer is 2, then guess 2, pay $1, and get the answer.
The worst case is that you pay $1.

Constraints:
- 1 <= n <= 200
"""


# 1 2 3

def get_money_amount(n):
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    def solve(i, j):
        if i >= j: return 0
        if dp[i][j] != -1: return dp[i][j]
        ans = float('inf')
        for k in range(i, j + 1):
            ans = min(ans, k + max(solve(i, k - 1), solve(k + 1, j)))
        dp[i][j] = ans
        return ans
            
    return solve(1, n)