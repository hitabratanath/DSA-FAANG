# Array Optimization - Solutions Template
from collections import Counter
def jump_game_solution(nums):
    """Jump Game Solutions"""
    farthest = 0
    for i in range(len(nums)):
        if farthest < i: return False
        farthest = max(farthest, i + nums[i])
    return True

def jump_game_ii_solution(nums):
    """Jump Game II Solutions"""
    step = 0
    left, right = 0, 0

    while right < len(nums) - 1:
        farthest = 0
        for i in range(left , right + 1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        step += 1
    return step

def gas_station_solution(gas, cost):
    """Gas Station Solutions"""
    if sum(gas) < sum(cost): return -1

    tank = 0
    start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    return start

def candy_solution(ratings):
    """Candy Solutions"""
    n = len(ratings)
    candies = [1] * n
    
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    for i in range(n - 2, -1, -1):
        if ratings[i] < ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)

def container_most_water_solution(height):
    """Container With Most Water Solutions"""
    n = len(height)
    left, right = 0, n - 1
    water, max_water = 0, 0
    
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

def trapping_rain_water_solution(height):
    """Trapping Rain Water Solutions"""
    n = len(height)
    max_greater_left, max_greater_right = [height[0]] * n, [height[n - 1]] * n
    water = 0
    
    for i in range(1, n):
        max_greater_left[i] = max(height[i], max_greater_left[i - 1])
    
    for i in range(n - 2, -1, -1):
        max_greater_right[i] = max(height[i], max_greater_right[i + 1])
    
    
    for i in range(n):
        water += min(max_greater_left[i], max_greater_right[i]) - height[i]
    return water

def maximum_subarray_solution():
    """Maximum Subarray Solutions"""
    pass

def hand_of_straights_solution(hand, groupSize):
    """Hand of Straights Solutions"""
    if len(hand) % groupSize != 0: return False

    hand = sorted(hand)
    counter = Counter(hand)

    i = 0
    while i < len(hand):
        for j in range(groupSize):
            if counter[hand[i] + j] == 0: return False
            counter[hand[i] + j] -= 1
            if counter[hand[i] + j] == 0: del counter[hand[i] + j]
        while i < len(hand) and hand[i] not in counter:
            i += 1
    return True                         