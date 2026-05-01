
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    C = int(data[0])
    colors = list(map(int, data[1:C+1]))

    if colors[0] != 1 or colors[-1] != 1:
        print(-1)
        return

    if C == 1:
        print(0)
        return

    INF = float('inf')
    dist = [INF] * C
    dist[0] = 0
    q = deque([0])

    while q:
        u = q.popleft()
        for v in [u-2, u-1, u+1, u+2]:
            if 0 <= v < C and colors[v] == 1 and dist[v] == INF:
                dist[v] = dist[u] + 1
                q.append(v)

    print(dist[-1] if dist[-1] != INF else -1)

if __name__ == "__main__":
    main()
