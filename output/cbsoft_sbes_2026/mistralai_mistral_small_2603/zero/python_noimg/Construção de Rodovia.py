
import sys
from collections import defaultdict, deque

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (N + 1)
    components = []
    for i in range(1, N + 1):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            component = []
            while queue:
                u = queue.popleft()
                component.append(u)
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            components.append(component)

    if len(components) == 1:
        print(-1)
        return

    comp_id = [0] * (N + 1)
    for i in range(len(components)):
        for u in components[i]:
            comp_id[u] = i

    for u in range(1, N + 1):
        for v in range(u + 1, N + 1):
            if comp_id[u] != comp_id[v]:
                print(u, v)
                return

    print(-1)

if __name__ == "__main__":
    main()
