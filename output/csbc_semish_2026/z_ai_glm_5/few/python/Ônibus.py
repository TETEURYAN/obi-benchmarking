import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        A = int(next(iterator))
        B = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    dist = [-1] * (N + 1)
    dist[A] = 0
    queue = deque([A])

    while queue:
        u = queue.popleft()
        if u == B:
            break
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    print(dist[B])

if __name__ == '__main__':
    solve()