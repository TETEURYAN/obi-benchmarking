import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])

edges = []
idx = 2
for _ in range(M):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    c = int(input_data[idx+2])
    edges.append((c, u, v))
    idx += 3

edges.sort(key=lambda x: x[0])

parent = list(range(N + 1))

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]

total_cost = 0
edges_used = 0

if N == 1:
    print(0)
    exit()

for c, u, v in edges:
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        parent[root_u] = root_v
        total_cost += c
        edges_used += 1
        if edges_used == N - 1:
            break

print(total_cost)