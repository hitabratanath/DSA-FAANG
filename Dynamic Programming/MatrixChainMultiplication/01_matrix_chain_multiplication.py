"""MATRIX CHAIN MULTIPLICATION

Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is to determine the order of matrix multiplication that minimizes the number of scalar multiplications.

Given an array arr[] which represents the chain of matrices such that the ith matrix Ai is of dimension arr[i-1] x arr[i].

Example 1:
Input: arr = [1, 2, 3, 4]
Output: 18
Explanation: There are 3 matrices of dimensions 1x2, 2x3, 3x4
Optimal order: ((A1 x A2) x A3) = 1*2*3 + 1*3*4 = 6 + 12 = 18

Example 2:
Input: arr = [40, 20, 30, 10, 30]
Output: 26000
Explanation: There are 4 matrices of dimensions 40x20, 20x30, 30x10, 10x30
Optimal order gives minimum multiplications.

Example 3:
Input: arr = [1, 2, 3]
Output: 6
Explanation: Only one way to multiply two matrices: 1*2*3 = 6

Constraints:
- 2 <= arr.length <= 100
- 1 <= arr[i] <= 100
"""

def matrix_chain_multiplication(arr):
    n = len(arr)
    dp = [[-1] * n for _ in range(n)]
    def solve(i, j):
        if i >= j:
            return 0
        if dp[i][j] != -1: return dp[i][j]
        ans = float('inf')
        for k in range(i, j):
            left = solve(i, k)
            right = solve(k + 1, j)
            temp_ans = left + right + arr[i - 1] * arr[k] * arr[j]
            ans = min(temp_ans, ans)
        dp[i][j] = ans
        return dp[i][j]
    
    return solve(1, n - 1)