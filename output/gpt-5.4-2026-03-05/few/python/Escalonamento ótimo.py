import sys
import heapq

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])

adj = [[] for _ in range(n)]
indeg = [0] * n

idx = 2
for _ in range(m):
    a = int(data[idx])
    b = int(data[idx + 1])
    idx += 2
    adj[a].append(b)
    indeg[b] += 1

heap = []
for i in range(n):
    if indeg[i] == 0:
        heapq.heappush(heap, i)

order = []
while heap:
    u = heapq.heappop(heap)
    order.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            heapq.heappush(heap, v)

if len(order) != n:
    sys.stdout.write("*\n")
else:
    sys.stdout.write("\n".join(map(str, order)))
    if n > 0:
        sys.stdout.write("\n")