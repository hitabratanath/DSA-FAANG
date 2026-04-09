# Miscellaneous Greedy - Solutions Template

def merge_triplets_solution(triplets, target):
    """Merge Triplets to Form Target Triplet Solutions"""
    max_triplet = [0, 0, 0]
    for triplet in triplets:
        if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
            max_triplet[0] = max(max_triplet[0], triplet[0])
            max_triplet[1] = max(max_triplet[1], triplet[1])
            max_triplet[2] = max(max_triplet[2], triplet[2])
    
    return max_triplet == target

def fractional_knapsack_solution(W, n, weight, value):
    """Fractional Knapsack Solutions"""
    items = [(value / weight, value, weight) for weight, value in zip(weight, value)]
    items = sorted(items, reverse=True)
    profit = 0
    
    # ratio, value, weight
    for i in range(len(items)):
        if items[i][2] <= W:
            W -= items[i][2]
            profit += items[i][1]
        else:
            profit += W * items[i][0]
            break
    return profit

def boats_to_save_people_solution(people, limit):
    """Boats to Save People Solutions"""
    people = sorted(people)
    count = 0
    i, j = 0, len(people) - 1
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        count += 1
        j -= 1
    return count

def two_city_scheduling_solution(costs):
    """Two City Scheduling Solutions"""
    costs = sorted([(cost[0] - cost[1], cost[0], cost[1]) for cost in costs])
    profit = 0
    for i in range(0, len(costs)//2):
        profit += costs[i][1]

    for i in range(len(costs)// 2, len(costs)):
        profit += costs[i][2]
    return profit