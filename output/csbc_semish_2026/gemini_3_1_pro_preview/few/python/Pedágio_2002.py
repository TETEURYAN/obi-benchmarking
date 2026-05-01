import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

idx = 0
test_case = 1
while idx < len(input_data):
    C = int(input_data[idx])
    E = int(input_data[idx+1])
    L = int(input_data[idx+2])
    P = int(input_data[idx+3])
    idx += 4
    
    if C == 0 and E == 0 and L == 0 and P == 0:
        break
        
    adj = [[] for _ in range(C + 1)]
    for _ in range(E):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    distances = [-1] * (C + 1)
    distances[L] = 0
    queue = [L]
    
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        
        if distances[u] == P:
            continue
            
        for v in adj[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 1
                queue.append(v)
                
    reachable = []
    for i in range(1, C + 1):
        if i != L and distances[i] != -1 and distances[i] <= P:
            reachable.append(i)
            
    print(f"Teste {test_case}")
    if reachable:
        print(*(reachable))
    else:
        print()
    print()
    
    test_case += 1