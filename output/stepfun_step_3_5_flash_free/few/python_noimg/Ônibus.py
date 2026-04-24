import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    dist = [-1] * (n + 1)
    q = deque()
    dist[a] = 0
    q.append(a)
    
    while q:
        u = q.popleft()
        if u == b:
            break
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    
    print(dist[b])

if __name__ == "__main__":
    main()