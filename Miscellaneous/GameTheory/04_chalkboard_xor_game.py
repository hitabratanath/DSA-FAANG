"""CHALKBOARD XOR GAME (LeetCode 810)

Alice and Bob take turns erasing one number from the chalkboard, with Alice starting first.
If the XOR of all remaining numbers becomes 0 after a player's turn, that player loses.
If a player has no numbers to erase, that player also loses.

Return true if Alice wins assuming both play optimally.

Example 1:
Input: nums = [1, 1, 2]
Output: False
Explanation: Alice has two choices: erase 1 or erase 2.
If she erases 1, XOR = 1^2 = 3. Bob erases 1, XOR = 2. Alice erases 2, XOR = 0. Alice loses.
If she erases 2, XOR = 1^1 = 0. Alice loses.

Example 2:
Input: nums = [0, 1]
Output: True

Example 3:
Input: nums = [1, 2, 3]
Output: True

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] < 2^16
"""

def xor_game(nums):
    pass
