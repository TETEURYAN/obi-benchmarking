import sys
import heapq

data = sys.stdin.read().split()
if not data:
    sys.exit()

c = int(data[0])
n = int(data[1])

heap = [0] * c
heapq.heapify(heap)

ans = 0
idx = 2

for _ in range(n):
    t = int(data[idx])
    d = int(data[idx + 1])
    idx += 2

    free_time = heapq.heappop(heap)
    start = t if free_time <= t else free_time
    if start - t > 20:
        ans += 1
    heapq.heappush(heap, start + d)

print(ans)