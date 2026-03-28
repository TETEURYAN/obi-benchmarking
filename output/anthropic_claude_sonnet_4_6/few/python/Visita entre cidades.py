import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    A = int(data[idx]); idx+=1
    B = int(data[idx]); idx+=1
    
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        p = int(data[idx]); idx+=1
        q = int(data[idx]); idx+=1
        d = int(data[idx]); idx+=1
        adj[p].append((q, d))
        adj[q].append((p, d))
    
    dist = [-1] * (N+1)
    dist[A] = 0
    queue = deque([A])
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                queue.append(v)
    
    print(dist[B])

main()