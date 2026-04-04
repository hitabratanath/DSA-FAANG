"""HAND OF STRAIGHTS

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

Constraints:
- 1 <= hand.length <= 10^4
- 0 <= hand[i] <= 10^9
- 1 <= groupSize <= hand.length

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
from collections import Counter
def is_n_straight_hand(hand, groupSize):
    if len(hand) % groupSize != 0: return False

    hand = sorted(hand)
    counter = Counter(hand)

    i = 0
    while i < len(hand):
        for j in range(groupSize):
            if counter[hand[i] + j] == 0: return False
            counter[hand[i] + j] -= 1
            if counter[hand[i] + j] == 0: del counter[hand[i] + j]
        while i < len(hand) and hand[i] not in counter:
            i += 1
    return True