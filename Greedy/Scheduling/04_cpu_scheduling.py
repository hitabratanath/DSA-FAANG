"""CPU SCHEDULING - SHORTEST JOB FIRST

Given n processes with their burst times, the task is to find average waiting time and average turn around time using shortest job first scheduling algorithm.

The shortest job first (SJF) or shortest job next, is a scheduling policy that selects the waiting process with the smallest execution time to execute next.

Example 1:
Input: processes = [1, 2, 3, 4], burst_time = [6, 8, 7, 3]
Output: Average waiting time = 7.00, Average turnaround time = 13.25
Explanation:
Process execution order: P4, P1, P3, P2
P4: waiting_time = 0, turnaround_time = 3
P1: waiting_time = 3, turnaround_time = 9
P3: waiting_time = 9, turnaround_time = 16
P2: waiting_time = 16, turnaround_time = 24

Example 2:
Input: processes = [1, 2, 3], burst_time = [10, 5, 8]
Output: Average waiting time = 7.33, Average turnaround time = 15.00

Constraints:
- 1 <= n <= 10^5
- 1 <= burst_time[i] <= 100

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def shortest_job_first(processes, burst_time):
    pass