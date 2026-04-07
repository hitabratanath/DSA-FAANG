"""MINIMUM PLATFORMS

Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the
 railway station so that no train waits.

Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never
 be the same for a train but we can have arrival time of one train equal to departure time of the other. 
 At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. 
 In such cases, we need different platforms.

Example 1:
Input: arr[] = [9:00, 9:40, 9:50, 11:00, 15:00, 18:00]
       dep[] = [9:10, 12:00, 11:20, 11:30, 19:00, 20:00]
Output: 3
Explanation: Minimum 3 platforms are required to safely arrive and depart all trains.

Example 2:
Input: arr[] = [9:00, 9:40]
       dep[] = [9:10, 12:00]
Output: 1
Explanation: Only 1 platform is required.

Constraints:
- 1 <= n <= 50000
- 0000 <= arr[i] <= dep[i] <= 2359

Time Complexity: O(n log n)
Space Complexity: O(1)

9---------910
                 940-----------1200
"""

def find_platform(arr, dep, n):
    pass