import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        mi = int(data[idx]); idx += 1
        for _ in range(mi):
            xj = int(data[idx]); idx += 1
            adj[i].append(xj)
    
    color = [-1] * (n + 1)
    color[1] = 0
    
    queue = deque([1])
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                queue.append(v)
    
    team0 = []
    team1 = []
    
    for i in range(1, n + 1):
        if color[i] == 0:
            team0.append(i)
        else:
            team1.append(i)
    
    print(*team0)
    print(*team1)

solve()