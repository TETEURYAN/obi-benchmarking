import sys
import heapq

data = sys.stdin.read().split()
idx = 0
N = int(data[idx])
idx += 1
M = int(data[idx])
idx += 1
T = [int(data[idx + i]) for i in range(N)]
idx += N
F = [int(data[idx + i]) for i in range(M)]
idx += M

T.sort(reverse=True)

heap = []
for j in range(M):
    heapq.heappush(heap, (0, j))

cars_per_mech = [[] for _ in range(M)]

for ti in T:
    time, j = heapq.heappop(heap)
    cars_per_mech[j].append(ti)
    new_time = time + ti * F[j]
    heapq.heappush(heap, (new_time, j))

total = 0
for j in range(M):
    if not cars_per_mech[j]:
        continue
    sorted_cars = sorted(cars_per_mech[j])
    prefix = 0
    for t in sorted_cars:
        total += prefix
        prefix += t * F[j]

print(total)