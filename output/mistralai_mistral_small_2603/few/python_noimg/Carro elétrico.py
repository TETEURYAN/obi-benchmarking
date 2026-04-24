
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    X = int(data[0])
    Y = int(data[1])
    N = int(data[2])
    A = int(data[3])

    cities = []
    for i in range(4, 4 + 2 * N, 2):
        x = int(data[i])
        y = int(data[i+1])
        cities.append((x, y))

    adj = [[] for _ in range(N+1)]
    for i in range(N):
        x1, y1 = cities[i]
        for j in range(i+1, N):
            x2, y2 = cities[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            if dist <= A:
                adj[i+1].append(j+1)
                adj[j+1].append(i+1)

    visited = [False] * (N+1)
    q = deque()
    q.append(1)
    visited[1] = True
    components = 0

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    components = sum(1 for i in range(1, N+1) if not visited[i])
    print(components)

if __name__ == "__main__":
    main()
