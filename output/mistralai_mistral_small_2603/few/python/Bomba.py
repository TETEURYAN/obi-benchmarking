
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print('*')
        return

    idx = 0
    N = int(data[idx]); idx += 1
    E = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1

    adj = [[] for _ in range(N)]
    for _ in range(M):
        A = int(data[idx]); idx += 1
        B = int(data[idx]); idx += 1
        T = int(data[idx]); idx += 1
        adj[A].append((B, T))

    INF = float('inf')
    dist = [INF] * N
    dist[E] = 0
    q = deque()
    q.append(E)

    while q:
        u = q.popleft()
        for (v, T) in adj[u]:
            time = dist[u] + 1
            if T == 1:
                if time % 3 == 0:
                    new_time = time
                else:
                    new_time = time + (3 - (time % 3))
            else:
                if time % 3 != 0:
                    new_time = time
                else:
                    new_time = time + 1
            if new_time < dist[v]:
                dist[v] = new_time
                q.append(v)

    if dist[S] == INF:
        print('*')
    else:
        print(dist[S])

if __name__ == '__main__':
    main()
