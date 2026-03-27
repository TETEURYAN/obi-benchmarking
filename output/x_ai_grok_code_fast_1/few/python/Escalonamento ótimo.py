import sys
import heapq

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])

graph = [[] for _ in range(N)]
indegree = [0] * N

idx = 2
for _ in range(M):
    A = int(input_data[idx])
    B = int(input_data[idx + 1])
    graph[A].append(B)
    indegree[B] += 1
    idx += 2

pq = []
for i in range(N):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

order = []
while pq:
    task = heapq.heappop(pq)
    order.append(task)
    for neighbor in graph[task]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            heapq.heappush(pq, neighbor)

if len(order) == N:
    for task in order:
        print(task)
else:
    print("*")