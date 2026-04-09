"""MAXIMUM XOR OF TWO NUMBERS IN AN ARRAY

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

Constraints:
- 1 <= nums.length <= 2 * 10^5
- 0 <= nums[i] <= 2^31 - 1

Approach: Use Trie to store binary representation of numbers
- Insert all numbers in binary trie
- For each number, try to find the number that gives maximum XOR
- At each bit position, try to go opposite direction for maximum XOR

Time Complexity: O(N * 32) where N is array length
Space Complexity: O(N * 32) for the trie
"""

def findMaximumXOR(nums):
    pass