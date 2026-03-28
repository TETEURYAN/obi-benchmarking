import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = int(next(it))
    b = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    visited = [False] * (n + 1)
    queue = deque()
    queue.append((a, 0))
    visited[a] = True
    
    while queue:
        u, d = queue.popleft()
        if u == b:
            print(d)
            return
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, d + w))

if __name__ == "__main__":
    main()