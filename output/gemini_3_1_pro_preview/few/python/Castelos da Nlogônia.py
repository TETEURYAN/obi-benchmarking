import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

adj = [[] for _ in range(n + 1)]
idx = 2
for _ in range(n - 1):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

colors = [0] * (n + 1)

for _ in range(m):
    p = int(input_data[idx])
    q = int(input_data[idx+1])
    c = int(input_data[idx+2])
    idx += 3
    
    queue = [p]
    parent = {p: -1}
    
    for u in queue:
        if u == q:
            break
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                queue.append(v)
                
    curr = q
    while curr != -1:
        colors[curr] = c
        curr = parent[curr]

print(*(colors[1:]))