import sys
import heapq

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
m = data[1]
T = data[2:2 + n]
F = data[2 + n:2 + n + m]

T.sort()
F.sort()

heap = []
for f in F:
    heap.append((0, f, 0))  # (incremento marginal atual, fator, quantidade já atribuída)
heapq.heapify(heap)

ans = 0

for t in T:
    inc, f, k = heapq.heappop(heap)
    ans += inc * t
    k += 1
    heapq.heappush(heap, (k * f, f, k))

print(ans)