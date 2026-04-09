from collections import Counter, deque
import heapq

# Scheduling - Solutions Template

def job_sequencing_solution(jobs):
    """Job Sequencing with Deadlines Solutions"""
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    
    last_deadline = -1
    for i in range(len(jobs)):
        last_deadline = max(last_deadline, jobs[i][1])
    
    jobs_day = [-1] * (last_deadline + 1)
    
    profit = 0
    for i in range(len(jobs)):
        day = jobs[i][1]
        while day > -1 and jobs_day[day] != -1:
            day -= 1
        if day >= 0:
            jobs_day[day] = jobs[i][0]
            profit += jobs[i][2]
    return profit

def task_scheduler_solution(tasks, n):
    """Task Scheduler Solutions"""
    counter = Counter(tasks)
    heap = [-cnt for cnt in counter.values()]
    heapq.heapify(heap)
    
    queue = deque([])
    time = 0
    
    while heap or queue:
        time += 1
        if heap:
            cnt = 1 + heapq.heappop(heap)
            if cnt:
                queue.append((cnt, time + n))
        if queue and queue[0][1] == time:
            heapq.heappush(heap, queue.popleft()[0])
    return time

def minimum_platforms_solution(arr, dep, n):
    """Minimum Platforms Solutions"""
    arr = sorted(arr)
    dep = sorted(dep)
    
    count, max_count = 0, 0
    i, j = 0, 0
    
    while i < n:
        if arr[i] <= dep[j]:
            count += 1
            max_count = max(max_count, count)
            i += 1
        else:
            count -= 1
            j += 1
    return max_count

def cpu_scheduling_solution():
    """CPU Scheduling (SJF) Solutions"""
    pass

def single_threaded_cpu_solution(tasks):
    """Single-Threaded CPU Solutions"""
    tasks = [(task[0], task[1], idx) for idx, task in enumerate(tasks)]
    tasks = sorted(tasks)
    time = 0
    result = []
    heap = []
    n = len(tasks)
    i = 0
    while i < n or heap:
        if not heap and i < n:
            time = tasks[i][0]
        
        while i < n and tasks[i][0] <= time:
            heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
            i += 1
        processing_time, idx = heapq.heappop(heap)
        time += processing_time
        result.append(idx)
    
    return result