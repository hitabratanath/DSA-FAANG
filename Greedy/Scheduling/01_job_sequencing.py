"""JOB SEQUENCING WITH DEADLINES

Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. It is also given that every job takes a single unit of time, so the minimum possible deadline for any job is 1. How to maximize total profit if only one job can be scheduled at a time.

Example 1:
Input: jobs = [['a', 4, 20], ['b', 1, 10], ['c', 1, 40], ['d', 1, 30]]
Output: ['c', 'a'], 60
Explanation: 
Job 'c' has profit 40 and deadline 1, so it should be done first.
Job 'a' has profit 20 and deadline 4, so it can be done in slot 2.
Total profit = 40 + 20 = 60

Example 2:
Input: jobs = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27], ['d', 1, 25], ['e', 3, 15]]
Output: ['a', 'c', 'e'], 142
Explanation: We can schedule jobs 'a', 'c', and 'e' to get maximum profit.

Constraints:
- 1 <= jobs.length <= 10^5
- Each job has format [id, deadline, profit]
- 1 <= deadline <= n
- 1 <= profit <= 10^4

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

def job_scheduling(jobs):
    pass