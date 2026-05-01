
import sys
from heapq import heappush, heappop

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    V = int(next(it))
    N = int(next(it))
    M = int(next(it))

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a = int(next(it))
        b = int(next(it))
        t = int(next(it))
        p = int(next(it))
        graph[a].append((b, t, p))
        graph[b].append((a, t, p))

    X = int(next(it))
    Y = int(next(it))

    INF = float('inf')
    dp = [[INF] * (V+1) for _ in range(N+1)]
    dp[X][0] = 0
    heap = []
    heappush(heap, (0, X, 0))

    while heap:
        current_time, u, current_cost = heappop(heap)
        if u == Y:
            print(current_time)
            return
        if current_time > dp[u][current_cost]:
            continue
        for (v, t, p) in graph[u]:
            new_cost = current_cost + p
            if new_cost > V:
                continue
            new_time = current_time + t
            if new_time < dp[v][new_cost]:
                dp[v][new_cost] = new_time
                heappush(heap, (new_time, v, new_cost))

    min_time = INF
    for cost in range(V+1):
        if dp[Y][cost] < min_time:
            min_time = dp[Y][cost]

    print(min_time if min_time != INF else -1)

if __name__ == "__main__":
    main()
