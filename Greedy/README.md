# Greedy Algorithms - FAANG Interview Preparation

This folder contains a comprehensive collection of greedy algorithm problems organized by patterns, covering all NeetCode 150 greedy problems and additional high-frequency FAANG interview questions.

## 📁 Folder Structure

### 🎯 ActivitySelection/
**Pattern**: Interval scheduling and optimization
- Activity Selection Problem
- Meeting Rooms I & II
- Non-overlapping Intervals
- Merge Intervals
- Insert Interval

### 🔢 ArrayOptimization/
**Pattern**: Greedy array traversal and optimization
- **NeetCode 150**: Jump Game, Jump Game II, Gas Station, Maximum Subarray, Hand of Straights
- Additional: Candy, Container With Most Water, Trapping Rain Water

### 🔤 StringGreedy/
**Pattern**: String manipulation using greedy approach
- **NeetCode 150**: Partition Labels, Valid Parenthesis String

### 🔀 Miscellaneous/
**Pattern**: Various greedy problems
- **NeetCode 150**: Merge Triplets to Form Target Triplet

## 🎯 NeetCode 150 Coverage

✅ **All 8 NeetCode 150 Greedy Problems Included:**
1. Maximum Subarray (Kadane's Algorithm)
2. Jump Game
3. Jump Game II  
4. Gas Station
5. Hand of Straights
6. Merge Triplets to Form Target Triplet
7. Partition Labels
8. Valid Parenthesis String



## 🔑 Key Patterns

- **Kadane's Algorithm**: Maximum subarray problems
- **Greedy Choice Property**: Jump games, gas station
- **Interval Management**: Meeting rooms, merge intervals
- **Two-Pointer Technique**: Valid parenthesis, container problems
- **Circular Array Handling**: Gas station
- **Consecutive Grouping**: Hand of straights

## 💡 Tips for Success

1. **Understand the Greedy Choice**: Always identify what makes a choice "greedy"
2. **Prove Optimality**: Ensure your greedy choice leads to optimal solution
3. **Pattern Recognition**: Group similar problems by their greedy strategy
4. **Time Complexity**: Most greedy solutions are O(n) or O(n log n)
5. **Edge Cases**: Always consider boundary conditions

## 🚀 Getting Started - Optimal Learning Order

### **Phase 1: Foundation (Days 1-3)**
**Goal**: Build core greedy intuition

1. **`ArrayOptimization/07_maximum_subarray.py`** - Maximum Subarray
   - **Why First**: Classic Kadane's algorithm, simplest greedy pattern
   - **Pattern**: Local vs global optimum decision making
   - **Key Insight**: Sometimes "restart" is better than "continue"

2. **`ArrayOptimization/01_jump_game.py`** - Jump Game
   - **Pattern**: Greedy reachability (can we reach the goal?)
   - **Key Insight**: Track furthest reachable position

3. **`StringGreedy/02_valid_parenthesis_string.py`** - Valid Parenthesis String
   - **Pattern**: Range-based greedy (min/max possible states)
   - **Key Insight**: Track range of possible open parentheses

### **Phase 2: Interval Mastery (Days 4-8)**
**Goal**: Master interval-based greedy patterns

4. **`ActivitySelection/02_meeting_rooms.py`** - Meeting Rooms
   - **Pattern**: Basic interval overlap detection
   - **Key Insight**: Sort by start time, check consecutive overlaps

5. **`ActivitySelection/05_merge_intervals.py`** - Merge Intervals
   - **Pattern**: Interval merging
   - **Key Insight**: Sort first, then merge overlapping intervals

6. **`ActivitySelection/04_non_overlapping_intervals.py`** - Non-overlapping Intervals
   - **Pattern**: Interval scheduling maximization
   - **Key Insight**: Sort by end time, pick earliest ending intervals

7. **`StringGreedy/01_partition_labels.py`** - Partition Labels
   - **Pattern**: Interval partitioning based on constraints
   - **Key Insight**: Find last occurrence, extend partition boundary

8. **`ActivitySelection/03_meeting_rooms_ii.py`** - Meeting Rooms II
   - **Pattern**: Resource allocation optimization
   - **Key Insight**: Track active intervals using min-heap

### **Phase 3: Advanced Array Optimization (Days 9-14)**
**Goal**: Complex greedy decision making

9. **`ArrayOptimization/02_jump_game_ii.py`** - Jump Game II
   - **Pattern**: Greedy optimization (minimum steps)
   - **Key Insight**: BFS-like approach with greedy choices

10. **`ArrayOptimization/03_gas_station.py`** - Gas Station
    - **Pattern**: Circular array + greedy starting point
    - **Key Insight**: If total gas ≥ total cost, solution exists

11. **`ArrayOptimization/08_hand_of_straights.py`** - Hand of Straights
    - **Pattern**: Consecutive grouping with frequency management
    - **Key Insight**: Always start groups with smallest available number

12. **`ArrayOptimization/04_candy.py`** - Candy
    - **Pattern**: Two-pass greedy with constraints
    - **Key Insight**: Left-to-right pass, then right-to-left pass

13. **`ArrayOptimization/05_container_with_most_water.py`** - Container With Most Water
    - **Pattern**: Two-pointer greedy optimization
    - **Key Insight**: Move pointer with smaller height

14. **`ArrayOptimization/06_trapping_rain_water.py`** - Trapping Rain Water
    - **Pattern**: Two-pointer with running max tracking
    - **Key Insight**: Water level determined by minimum of left/right max

### **Phase 4: Scheduling & Resource Management (Days 15-19)**
**Goal**: Optimize resource allocation and task scheduling

15. **`Scheduling/02_task_scheduler.py`** - Task Scheduler
    - **Pattern**: Frequency-based scheduling with constraints
    - **Key Insight**: Most frequent task determines minimum time

16. **`Scheduling/03_minimum_platforms.py`** - Minimum Platforms
    - **Pattern**: Event-based resource allocation
    - **Key Insight**: Track arrivals and departures separately

17. **`Scheduling/01_job_sequencing.py`** - Job Sequencing with Deadlines
    - **Pattern**: Deadline-aware profit maximization
    - **Key Insight**: Sort by profit, assign to latest possible slot

18. **`Scheduling/04_cpu_scheduling.py`** - CPU Scheduling (SJF)
    - **Pattern**: Shortest job first optimization
    - **Key Insight**: Minimize average waiting time

19. **`Scheduling/05_single_threaded_cpu.py`** - Single-Threaded CPU
    - **Pattern**: Priority queue with time-based availability
    - **Key Insight**: Process shortest available task at each time

### **Phase 5: Graph Algorithms (Days 20-24)**
**Goal**: Master graph-based greedy algorithms

20. **`GraphGreedy/02_dijkstra_shortest_path.py`** - Dijkstra's Algorithm
    - **Pattern**: Greedy shortest path selection
    - **Key Insight**: Always pick unvisited node with minimum distance

21. **`GraphGreedy/03_network_delay_time.py`** - Network Delay Time
    - **Pattern**: Single-source shortest path application
    - **Key Insight**: Find maximum of all shortest paths

22. **`GraphGreedy/01_minimum_spanning_tree.py`** - Minimum Spanning Tree
    - **Pattern**: Edge selection with cycle detection
    - **Key Insight**: Always pick minimum weight edge that doesn't create cycle

23. **`GraphGreedy/04_cheapest_flights_k_stops.py`** - Cheapest Flights K Stops
    - **Pattern**: Constrained shortest path
    - **Key Insight**: Bellman-Ford with stop limitation

24. **`GraphGreedy/05_path_with_minimum_effort.py`** - Path With Minimum Effort
    - **Pattern**: Modified Dijkstra for 2D grid
    - **Key Insight**: Minimize maximum edge weight in path

### **Phase 6: Advanced Multi-dimensional & Mastery (Days 25-30)**
**Goal**: Handle complex constraints and achieve mastery

25. **`Miscellaneous/01_merge_triplets_target.py`** - Merge Triplets
    - **Pattern**: Multi-dimensional greedy filtering
    - **Key Insight**: Filter valid triplets, then check coverage

26. **`ActivitySelection/06_insert_interval.py`** - Insert Interval
    - **Pattern**: Interval insertion with merging
    - **Key Insight**: Three phases - before, overlap, after

27. **`ActivitySelection/01_activity_selection.py`** - Activity Selection
    - **Pattern**: Classic greedy algorithm foundation
    - **Key Insight**: Sort by finish time, pick non-overlapping activities

28. **`Miscellaneous/02_fractional_knapsack.py`** - Fractional Knapsack
    - **Pattern**: Value-to-weight ratio optimization
    - **Key Insight**: Sort by value/weight ratio, take greedily

29. **`Miscellaneous/03_boats_to_save_people.py`** - Boats to Save People
    - **Pattern**: Two-pointer pairing optimization
    - **Key Insight**: Pair heaviest with lightest when possible

30. **`Miscellaneous/04_two_city_scheduling.py`** - Two City Scheduling
    - **Pattern**: Cost difference optimization
    - **Key Insight**: Sort by cost difference, split optimally

## 📈 **Pattern Recognition Milestones**

- **After Problem 3**: Understand basic greedy choice property
- **After Problem 8**: Master interval-based problems
- **After Problem 14**: Handle complex array optimization
- **After Problem 19**: Confident with scheduling algorithms
- **After Problem 24**: Expert in graph greedy algorithms
- **After Problem 30**: Complete mastery of all greedy patterns

## 🎯 **Weekly Practice Schedule**
- **Week 1 (Days 1-7)**: Foundation + Intervals (Problems 1-8)
- **Week 2 (Days 8-14)**: Array Optimization Mastery (Problems 9-14)
- **Week 3 (Days 15-21)**: Scheduling + Graph Intro (Problems 15-21)
- **Week 4 (Days 22-28)**: Graph Mastery + Advanced (Problems 22-28)
- **Week 5 (Days 29-30)**: Final Mastery + Review (Problems 29-30)

## 🏆 **Mastery Checkpoints**

### **After Week 1**: Can solve basic greedy problems
- Identify when greedy approach is optimal
- Handle simple interval problems
- Understand local vs global optimum

### **After Week 2**: Confident with array optimizations
- Master two-pointer techniques
- Handle circular array problems
- Solve complex constraint problems

### **After Week 3**: Expert in scheduling algorithms
- Optimize resource allocation
- Handle priority-based scheduling
- Solve real-world scheduling problems

### **After Week 4**: Graph algorithm mastery
- Implement shortest path algorithms
- Handle constrained graph problems
- Optimize network-based solutions

### **After Week 5**: Complete greedy mastery
- Recognize all major greedy patterns
- Choose optimal approaches quickly
- Ready for any FAANG greedy interview

## 💡 **Success Tips**
- **Before coding**: Always identify the greedy choice
- **After solving**: Write down the pattern used
- **Weekly review**: Group problems by similar patterns
- **Mock interviews**: Practice explaining your greedy strategy
- **Pattern journal**: Keep notes on when each pattern applies

Each problem includes detailed problem statement, examples, constraints, time/space complexity analysis, and function signature to implement.