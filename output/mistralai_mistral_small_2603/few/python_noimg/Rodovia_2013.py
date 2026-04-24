
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n):
        a = int(data[idx])
        b = int(data[idx + 1])
        adj[a].append(b)
        idx += 2

    visited = [False] * (n + 1)
    queue = deque()
    queue.append(1)
    visited[1] = True
    count = 1

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                count += 1
                queue.append(v)

    if count == n:
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()
