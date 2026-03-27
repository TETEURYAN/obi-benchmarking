
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
        p = int(data[idx])
        q = int(data[idx + 1])
        adj[p].append(q)
        adj[q].append(p)
        idx += 2

    if a == b:
        print(0)
        return

    visited = [False] * (n + 1)
    queue = deque()
    queue.append((a, 0))
    visited[a] = True

    while queue:
        current, dist = queue.popleft()
        if current == b:
            print(dist)
            return
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))

    print(-1)

if __name__ == "__main__":
    main()
