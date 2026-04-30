
import heapq

def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    idx += 2

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A = int(data[idx])
        B = int(data[idx+1])
        C = int(data[idx+2])
        idx += 3
        graph[A].append((B, C))
        graph[B].append((A, C))

    INF = float('inf')
    dist = [INF] * (N+1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        current_dist, u = heapq.heappop(heap)
        if u == N:
            break
        if current_dist > dist[u]:
            continue
        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(heap, (dist[v], v))

    print(dist[N])

if __name__ == "__main__":
    main()
