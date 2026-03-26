"""TARGET SUM

You are given an integer array nums and an integer target. You want to build an expression 
by adding '+' or '-' before each integer in nums and then concatenate all the integers.

Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Explanation: There are 5 ways: -1+1+1+1+1 = 3, +1-1+1+1+1 = 3, +1+1-1+1+1 = 3, +1+1+1-1+1 = 3, +1+1+1+1-1 = 3.

Example 2:
Input: nums = [1], target = 1
Output: 1
Explanation: Only one way: +1 = 1.

Example 3:
Input: nums = [1, 0], target = 1
Output: 2
Explanation: Two ways: +1+0 = 1, +1-0 = 1.

Constraints:
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000
"""

def target_sum(arr, sm, n):
    pass
