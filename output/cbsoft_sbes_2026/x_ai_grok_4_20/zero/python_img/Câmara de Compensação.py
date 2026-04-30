
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

has_positive = False
has_negative = False
for i in range(1, N + 1):
    if net[i] > 0:
        has_positive = True
    elif net[i] < 0:
        has_negative = True

if not has_positive or not has_negative:
    print("N")
    print(total)
    sys.exit(0)

def dfs(node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if graph[node][neighbor] > 0 and not visited[neighbor]:
            dfs(neighbor, visited, component)

visited = [False] * (N + 1)
can_reduce = False
min_total = 0

for i in range(1, N + 1):
    if not visited[i] and graph[i]:
        component = []
        dfs(i, visited, component)
        if len(component) > 1:
            can_reduce = True
        pos_sum = 0
        for u in component:
            for v in graph[u]:
                if graph[u][v] > 0:
                    pos_sum += graph[u][v]
        min_total += pos_sum

if can_reduce:
    print("S")
    print(min_total)
else:
    print("N")
    print(total)
