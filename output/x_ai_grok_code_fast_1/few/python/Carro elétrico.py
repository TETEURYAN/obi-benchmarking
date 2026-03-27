import sys

input_data = sys.stdin.read().split()
idx = 0
X = int(input_data[idx])
idx += 1
Y = int(input_data[idx])
idx += 1
N = int(input_data[idx])
idx += 1
A = int(input_data[idx])
idx += 1

cities = []
for i in range(N):
    x = int(input_data[idx])
    idx += 1
    y = int(input_data[idx])
    idx += 1
    cities.append((x, y))

# Build graph
adj = [[] for _ in range(N)]
max_dist = A // 100
for i in range(N):
    for j in range(i+1, N):
        dx = abs(cities[i][0] - cities[j][0])
        dy = abs(cities[i][1] - cities[j][1])
        if dx + dy <= max_dist:
            adj[i].append(j)
            adj[j].append(i)

# Count components
visited = [False] * N
components = 0
for i in range(N):
    if not visited[i]:
        components += 1
        stack = [i]
        visited[i] = True
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

print(components - 1)