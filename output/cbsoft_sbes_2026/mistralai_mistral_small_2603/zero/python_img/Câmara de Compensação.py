
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    M = int(data[idx])
    N = int(data[idx+1])
    idx += 2

    graph = defaultdict(dict)
    total_out = [0] * (N + 1)
    total_in = [0] * (N + 1)

    for _ in range(M):
        X = int(data[idx])
        V = int(data[idx+1])
        Y = int(data[idx+2])
        idx += 3

        if Y in graph[X]:
            graph[X][Y] += V
        else:
            graph[X][Y] = V
        total_out[X] += V
        total_in[Y] += V

    possible = False
    min_total = 0

    for i in range(1, N + 1):
        if total_out[i] != total_in[i]:
            possible = True
            break

    if not possible:
        print('N')
        print(sum(total_out[1:N+1]))
        return

    print('S')

    nodes = []
    for i in range(1, N + 1):
        if total_out[i] > 0:
            nodes.append(i)

    n = len(nodes)
    if n == 0:
        print(0)
        return

    INF = 10**18
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        u = nodes[i]
        for v in graph[u]:
            j = nodes.index(v)
            dist[i][j] = graph[u][v]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    min_total = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != INF:
                min_total += dist[i][j]

    print(min_total)

if __name__ == "__main__":
    main()
