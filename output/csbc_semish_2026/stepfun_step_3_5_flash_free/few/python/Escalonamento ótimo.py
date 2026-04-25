import sys
import heapq

data = sys.stdin.read().split()
if not data:
    exit()
it = iter(data)
n = int(next(it))
m = int(next(it))

if n == 0:
    exit()

adj = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(m):
    a = int(next(it))
    b = int(next(it))
    adj[a].append(b)
    indegree[b] += 1

heap = []
for i in range(n):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

order = []
while heap:
    u = heapq.heappop(heap)
    order.append(u)
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(heap, v)

if len(order) != n:
    print("*")
else:
    sys.stdout.write("\n".join(map(str, order)))
    if order:
        sys.stdout.write("\n")