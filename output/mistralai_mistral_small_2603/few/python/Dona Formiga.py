
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    S = int(data[0])
    T = int(data[1])
    P = int(data[2])
    heights = list(map(int, data[3:3+S]))

    adj = [[] for _ in range(S+1)]
    idx = 3 + S
    for _ in range(T):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (S + 1)
    queue = deque()
    queue.append((P, 0))
    visited[P] = True
    max_visited = 0

    while queue:
        current, count = queue.popleft()
        max_visited = max(max_visited, count)

        for neighbor in adj[current]:
            if not visited[neighbor] and heights[neighbor - 1] < heights[current - 1]:
                visited[neighbor] = True
                queue.append((neighbor, count + 1))

    print(max_visited)

if __name__ == "__main__":
    main()
