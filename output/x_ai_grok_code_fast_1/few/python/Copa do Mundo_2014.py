import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px = find(parent, x)
    py = find(parent, y)
    if px != py:
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
F = int(input_data[idx])
idx += 1
R = int(input_data[idx])
idx += 1

arestas_ferro = []
for _ in range(F):
    A = int(input_data[idx])
    B = int(input_data[idx + 1])
    C = int(input_data[idx + 2])
    arestas_ferro.append((C, A, B))
    idx += 3

arestas_rodo = []
for _ in range(R):
    I = int(input_data[idx])
    J = int(input_data[idx + 1])
    K = int(input_data[idx + 2])
    arestas_rodo.append((K, I, J))
    idx += 3

parent = list(range(N + 1))
rank = [0] * (N + 1)

arestas_ferro.sort()
custo_ferro = 0
for C, A, B in arestas_ferro:
    if find(parent, A) != find(parent, B):
        union(parent, rank, A, B)
        custo_ferro += C

arestas_rodo.sort()
custo_rodo = 0
for K, I, J in arestas_rodo:
    if find(parent, I) != find(parent, J):
        union(parent, rank, I, J)
        custo_rodo += K

print(custo_ferro + custo_rodo)