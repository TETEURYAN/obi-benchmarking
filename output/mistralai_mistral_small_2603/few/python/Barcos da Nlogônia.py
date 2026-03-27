
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    b = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(b):
        i = int(next(it))
        j = int(next(it))
        p = int(next(it))
        adj[i].append((j, p))
        adj[j].append((i, p))

    c = int(next(it))
    queries = []
    for _ in range(c):
        x = int(next(it))
        y = int(next(it))
        queries.append((x, y))

    max_p = [0] * (n + 1)
    visited = [False] * (n + 1)

    for x, y in queries:
        if x == y:
            print(0)
            continue

        q = deque()
        q.append((x, float('inf')))
        visited = [False] * (n + 1)
        visited[x] = True
        found = False
        result = 0

        while q and not found:
            current, current_min = q.popleft()
            for neighbor, p in adj[current]:
                if not visited[neighbor]:
                    new_min = min(current_min, p)
                    if neighbor == y:
                        result = new_min
                        found = True
                        break
                    visited[neighbor] = True
                    q.append((neighbor, new_min))

        print(result)

if __name__ == "__main__":
    main()
