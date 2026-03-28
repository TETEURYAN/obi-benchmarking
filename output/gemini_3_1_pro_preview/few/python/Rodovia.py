import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])

out_lists = [[] for _ in range(N + 1)]
out_sets = [set() for _ in range(N + 1)]

idx = 2
for _ in range(M):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    out_lists[u].append(v)
    out_sets[u].add(v)
    idx += 2
    
for u in range(1, N + 1):
    out_u = out_sets[u]
    if not out_lists[u]:
        continue
        
    out_u.add(u)
    for v in out_lists[u]:
        if not out_sets[v].issubset(out_u):
            for w in out_sets[v]:
                if w not in out_u:
                    print(f"{u} {w}")
                    exit()
    out_u.remove(u)
    
print("-1")