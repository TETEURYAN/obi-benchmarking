
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            component = []
            while queue:
                u = queue.popleft()
                component.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            components.append(component)

    selected = []
    for component in components:
        max_color = max(component)
        selected.append(max_color)

    selected.sort()
    print(len(selected))
    print(' '.join(map(str, selected)))

if __name__ == "__main__":
    main()
