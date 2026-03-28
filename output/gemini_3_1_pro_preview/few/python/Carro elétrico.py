import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

X = int(input_data[0])
Y = int(input_data[1])
N = int(input_data[2])
A = int(input_data[3])

cities = []
idx = 4
for _ in range(N):
    cities.append((int(input_data[idx]), int(input_data[idx+1])))
    idx += 2

parent = list(range(N))
rank = [0] * N

def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        if rank[root_i] < rank[root_j]:
            parent[root_i] = root_j
        elif rank[root_i] > rank[root_j]:
            parent[root_j] = root_i
        else:
            parent[root_j] = root_i
            rank[root_i] += 1
        return True
    return False

components = N
max_dist = A // 100

for i in range(N):
    xi, yi = cities[i]
    for j in range(i + 1, N):
        xj, yj = cities[j]
        if abs(xi - xj) + abs(yi - yj) <= max_dist:
            if union(i, j):
                components -= 1

print(components - 1)