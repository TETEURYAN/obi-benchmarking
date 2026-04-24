
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    n = int(data[0])
    d = int(data[1])
    points = []
    idx = 2
    for i in range(n):
        x = int(data[idx])
        y = int(data[idx+1])
        points.append((x, y))
        idx += 2

    adj = [[] for _ in range(n)]
    d_squared = d * d
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dist_sq = dx * dx + dy * dy
            if dist_sq <= d_squared:
                adj[i].append(j)
                adj[j].append(i)

    visited = [False] * n
    queue = deque()
    queue.append(0)
    visited[0] = True
    count = 1

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                count += 1
                queue.append(v)

    print('S' if count == n else 'N')

if __name__ == "__main__":
    main()
