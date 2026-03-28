import sys
import heapq

input_data = sys.stdin.read().split()
if not input_data:
    exit()

C = int(input_data[0])
N = int(input_data[1])

heap = [0] * C

ans = 0
idx = 2
for _ in range(N):
    T = int(input_data[idx])
    D = int(input_data[idx+1])
    idx += 2
    
    t_free = heapq.heappop(heap)
    
    if t_free - T > 20:
        ans += 1
        
    heapq.heappush(heap, max(T, t_free) + D)

print(ans)