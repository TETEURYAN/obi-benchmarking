
import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

index = 0
M = int(data[index])
index += 1
N = int(data[index])
index += 1

graph = [defaultdict(int) for _ in range(N + 1)]
net = [0] * (N + 1)
total = 0

for _ in range(M):
    X = int(data[index])
    index += 1
    V = int(data[index])
    index += 1
    Y = int(data[index])
    index += 1
    graph[X][Y] += V
    net[X] -= V
    net[Y] += V
    total += V

# Subtarefa A: check if can reduce
can_reduce = False
for u in range(1, N + 1):
    for v, val in list(graph[u].items()):
        if v in graph and u in graph[v]:
            common = min(val, graph[v][u])
            if common > 0:
                can_reduce = True
                break
    if can_reduce:
        break

if not can_reduce:
    for u in range(1, N + 1):
        if net[u] != 0:
            can_reduce = True
            break

print('S' if can_reduce else 'N')

# Subtarefa B: minimum total compensated = sum of positive net flows / 2
min_total = sum(max(0, net[i]) for i in range(1, N + 1)) // 2
print(min_total)
