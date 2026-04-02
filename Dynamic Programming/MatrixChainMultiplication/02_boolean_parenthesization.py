"""BOOLEAN PARENTHESIZATION / EVALUATE EXPRESSION TO TRUE

Given a boolean expression with the following symbols:
- 'T' --> true
- 'F' --> false
- '&' --> boolean AND
- '|' --> boolean OR  
- '^' --> boolean XOR

Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

Example 1:
Input: s = "T|T&F^T"
Output: 4
Explanation: The expression can be parenthesized in 4 ways to get True:
((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T), (T|((T&F)^T))

Example 2:
Input: s = "T^F|F"
Output: 2
Explanation: (T^(F|F)) and ((T^F)|F) both evaluate to True.

Example 3:
Input: s = "F&T^F"
Output: 2
Explanation: (F&(T^F)) and ((F&T)^F) both evaluate to True.

Constraints:
- 1 <= s.length <= 200
- s[i] is either 'T', 'F', '&', '|', or '^'
- The expression is guaranteed to be valid
"""

def count_ways_to_evaluate_true(s):
    def solve(i, j, is_true):
        if i == j:
            if is_true:
                return 1 if s[i] == 'T' else 0
            else: 
                return 1 if s[i] == 'F' else 0
        
        ans = 0
        for k in range(i + 1, j, 2):
            left_true = solve(i, k, True)
            left_false = solve(i, k, False)
            right_true = solve(k + 1, j, True)
            right_false = solve(k + 1, j, False)

            if is_true:
                if s[k] == '&':
                    ans += left_true * right_true
                elif s[k] == '|':
                    ans += left_true * right_true + left_true * right_false + left_false * right_true
                else:
                    ans += left_true * right_false + left_false * right_true
            else:
                if s[k] == '&':
                    ans += left_true * right_false + left_false * right_true + left_false * right_false
                elif s[k] == '|':
                    ans += left_false * right_false
                else:
                    ans += left_true * right_true + left_false * right_false
        return ans
    
    return solve(0, len(s) - 1, True)