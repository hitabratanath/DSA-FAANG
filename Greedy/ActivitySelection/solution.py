# Activity Selection - Solutions Template

def activity_selection_solution():
    """
    Activity Selection Problem Solutions
    """
def activity_selection(start, finish):
    activity = sorted(zip(start, finish), key=lambda x: x[1])
    count = 1
    finish = activity[0][1]
    
    for i in range(1, len(activity)):
        if activity[i][0] >= finish:
            count += 1
            finish = activity[i][1]
            
    return count

def meeting_rooms_solution():
    """
    Meeting Rooms Solutions
    """
    pass

def meeting_rooms_ii_solution():
    """
    Meeting Rooms II Solutions
    """
    pass

def non_overlapping_intervals_solution():
    """
    Non-overlapping Intervals Solutions
    """
    pass

def merge_intervals_solution():
    """
    Merge Intervals Solutions
    """
    pass

def insert_interval_solution(intervals, newInterval):
    """
    Insert Interval Solutions
    """
    i, n = 0, len(intervals)
    result = []

    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    while i < n:
        result.append(intervals[i])
        i += 1
    return result 