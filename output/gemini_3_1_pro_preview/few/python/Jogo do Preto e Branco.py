import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

L = int(input_data[0])
C = int(input_data[1])
P = int(input_data[2])

black_pieces = set()
idx = 3
for _ in range(P):
    r = int(input_data[idx])
    c = int(input_data[idx+1])
    black_pieces.add((r, c))
    idx += 2
    
candidates = set()
for r in range(1, L + 1):
    for c in range(1, C + 1):
        if (r, c) in black_pieces:
            continue
        
        is_candidate = False
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in black_pieces:
                is_candidate = True
                break
        
        if is_candidate:
            candidates.add((r, c))
            
left_nodes = []
for r, c in candidates:
    if (r + c) % 2 == 0:
        left_nodes.append((r, c))
        
graph = {u: [] for u in left_nodes}
for r, c in left_nodes:
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if (nr, nc) in candidates:
            graph[(r, c)].append((nr, nc))
            
match = {}
def dfs(u, visited):
    for v in graph[u]:
        if v not in visited:
            visited.add(v)
            if v not in match or dfs(match[v], visited):
                match[v] = u
                return True
    return False

max_matching = 0
for u in left_nodes:
    if dfs(u, set()):
        max_matching += 1
        
print(len(candidates) - max_matching)