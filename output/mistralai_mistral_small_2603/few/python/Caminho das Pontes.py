
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    idx += 2

    graph = [[] for _ in range(N + 2)]
    for _ in range(M):
        S = int(data[idx])
        T = int(data[idx+1])
        B = int(data[idx+2])
        idx += 3
        graph[S].append((T, B))
        graph[T].append((S, B))

    INF = float('inf')
    dist = [INF] * (N + 2)
    dist[0] = 0
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        current_dist, u = heapq.heappop(heap)
        if u == N + 1:
            break
        if current_dist > dist[u]:
            continue
        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(heap, (dist[v], v))

    print(dist[N + 1])

if __name__ == "__main__":
    main()
