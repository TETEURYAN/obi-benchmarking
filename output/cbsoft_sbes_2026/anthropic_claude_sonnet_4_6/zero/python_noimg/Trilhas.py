import sys

def calc_effort(heights):
    effort = 0
    for i in range(1, len(heights)):
        diff = heights[i] - heights[i-1]
        if diff > 0:
            effort += diff
    return effort

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    
    best_id = -1
    best_effort = float('inf')
    
    for trail_id in range(1, N+1):
        M = int(input_data[idx]); idx += 1
        heights = []
        for i in range(M):
            heights.append(int(input_data[idx])); idx += 1
        
        effort_forward = calc_effort(heights)
        effort_backward = calc_effort(heights[::-1])
        effort = min(effort_forward, effort_backward)
        
        if effort < best_effort:
            best_effort = effort
            best_id = trail_id
    
    print(best_id)

solve()