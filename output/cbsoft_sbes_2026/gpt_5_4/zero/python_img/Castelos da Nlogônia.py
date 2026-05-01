import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    for _ in range(m):
        p, q, c = map(int, input().split())
        
        parent = [-1] * (n + 1)
        parent[p] = 0
        dq = deque([p])
        
        while dq:
            u = dq.popleft()
            if u == q:
                break
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    dq.append(v)
        
        cur = q
        while cur != 0:
            color[cur] = c
            if cur == p:
                break
            cur = parent[cur]
    
    print(*color[1:])

if __name__ == "__main__":
    main()
