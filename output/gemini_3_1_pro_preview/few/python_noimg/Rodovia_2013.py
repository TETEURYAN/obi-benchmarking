import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

idx = 0
while idx < len(input_data):
    n = int(input_data[idx])
    idx += 1
    
    in_deg = [0] * (n + 1)
    out_deg = [0] * (n + 1)
    adj = [0] * (n + 1)
    
    for _ in range(n):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        out_deg[u] += 1
        in_deg[v] += 1
        adj[u] = v
        idx += 2
        
    possible = True
    for i in range(1, n + 1):
        if in_deg[i] != 1 or out_deg[i] != 1:
            possible = False
            break
            
    if not possible:
        print('N')
        continue
        
    curr = 1
    visited = 0
    for _ in range(n):
        curr = adj[curr]
        visited += 1
        if curr == 1:
            break
            
    if visited == n and curr == 1:
        print('S')
    else:
        print('N')