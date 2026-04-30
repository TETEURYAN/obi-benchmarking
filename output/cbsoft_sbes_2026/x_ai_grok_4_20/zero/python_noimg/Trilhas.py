
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
index = 1
best_effort = float('inf')
best_id = -1

for trail_id in range(1, N + 1):
    M = int(data[index])
    index += 1
    H = [int(data[index + i]) for i in range(M)]
    index += M
    
    # Forward direction
    effort_forward = 0
    for i in range(1, M):
        if H[i] > H[i-1]:
            effort_forward += H[i] - H[i-1]
    
    # Backward direction
    effort_backward = 0
    for i in range(M-2, -1, -1):
        if H[i] > H[i+1]:
            effort_backward += H[i] - H[i+1]
    
    min_effort = min(effort_forward, effort_backward)
    
    if min_effort < best_effort or (min_effort == best_effort and trail_id < best_id):
        best_effort = min_effort
        best_id = trail_id

print(best_id)
