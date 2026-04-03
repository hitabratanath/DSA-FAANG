"""VALID PARENTHESIS STRING

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Constraints:
- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def check_valid_string(s):
    min_count, max_count = 0, 0
    for c in s:
        if c == '(':
            min_count += 1
            max_count += 1
        elif c == ')':
            min_count = max(min_count - 1, 0)
            max_count -= 1
        else:
            min_count = max(min_count - 1, 0)
            max_count += 1
        if max_count < 0:
            return False
        
    return min_count == 0

