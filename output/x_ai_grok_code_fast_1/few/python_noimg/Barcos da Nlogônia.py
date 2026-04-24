import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
B = int(input_data[idx])
idx += 1

edges = []
for _ in range(B):
    I = int(input_data[idx])
    J = int(input_data[idx + 1])
    P = int(input_data[idx + 2])
    edges.append((P, I, J))
    idx += 3

C = int(input_data[idx])
idx += 1

queries = []
for _ in range(C):
    X = int(input_data[idx])
    Y = int(input_data[idx + 1])
    queries.append((X, Y))
    idx += 2

edges.sort(reverse=True)

respostas = [0] * C
queries_per_comp = [[] for _ in range(N + 1)]
for i, (X, Y) in enumerate(queries):
    queries_per_comp[X].append((Y, i))

parent = list(range(N + 1))
rank = [0] * (N + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(u, v, p):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return
    if rank[pu] < rank[pv]:
        # process queries_per_comp[pu]
        for y, idx in queries_per_comp[pu]:
            if find(y) == pv:
                respostas[idx] = p
        parent[pu] = pv
        queries_per_comp[pv].extend(queries_per_comp[pu])
        queries_per_comp[pu] = []
    else:
        # process queries_per_comp[pv]
        for y, idx in queries_per_comp[pv]:
            if find(y) == pu:
                respostas[idx] = p
        if rank[pu] == rank[pv]:
            rank[pu] += 1
        parent[pv] = pu
        queries_per_comp[pu].extend(queries_per_comp[pv])
        queries_per_comp[pv] = []

for p, i, j in edges:
    union(i, j, p)

for ans in respostas:
    print(ans)