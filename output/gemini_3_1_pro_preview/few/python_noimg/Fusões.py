import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
K = int(input_data[1])

parent = list(range(N + 1))
rank = [0] * (N + 1)

def find(i):
    root = i
    while parent[root] != root:
        root = parent[root]
    curr = i
    while curr != root:
        nxt = parent[curr]
        parent[curr] = root
        curr = nxt
    return root

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

idx = 2
out = []
for _ in range(K):
    op = input_data[idx]
    u = int(input_data[idx+1])
    v = int(input_data[idx+2])
    idx += 3
    
    if op == 'F':
        union(u, v)
    else:
        if find(u) == find(v):
            out.append('S')
        else:
            out.append('N')
            
if out:
    print('\n'.join(out))