import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        if c == 0:
            adj[a].append(b)
            adj[b].append(a)
    visited = [False]*(n+1)
    total_pairs = n*(n-1)//2
    subtrai = 0
    for i in range(1, n+1):
        if not visited[i]:
            q = deque([i])
            visited[i] = True
            count = 0
            while q:
                u = q.popleft()
                count += 1
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            subtrai += count*(count-1)//2
    print(total_pairs - subtrai)

if __name__ == "__main__":
    main()