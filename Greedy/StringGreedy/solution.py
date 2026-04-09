# String Greedy - Solutions Template

def partition_labels_solution():
    """Partition Labels Solutions"""
    pass

def valid_parenthesis_string_solution():
    """Valid Parenthesis String Solutions"""
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