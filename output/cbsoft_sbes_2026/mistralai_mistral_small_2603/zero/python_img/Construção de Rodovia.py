
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n+1)
    components = []
    for i in range(1, n+1):
        if not visited[i]:
            comp = []
            queue = deque([i])
            visited[i] = True
            while queue:
                u = queue.popleft()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            components.append(comp)

    if len(components) == 1:
        print(-1)
        return

    comp_id = [0] * (n+1)
    for idx, comp in enumerate(components):
        for u in comp:
            comp_id[u] = idx

    for u in range(1, n+1):
        for v in adj[u]:
            if comp_id[u] != comp_id[v]:
                print(u, v)
                return

    for i in range(len(components)):
        for j in range(i+1, len(components)):
            u = components[i][0]
            v = components[j][0]
            print(u, v)
            return

    print(-1)

if __name__ == "__main__":
    main()
