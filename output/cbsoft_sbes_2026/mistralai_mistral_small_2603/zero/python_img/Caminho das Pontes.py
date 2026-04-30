
import heapq

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N, M = map(int, input[ptr:ptr+2])
    ptr += 2

    adj = [[] for _ in range(N + 2)]

    for _ in range(M):
        S, T, B = map(int, input[ptr:ptr+3])
        ptr += 3
        adj[S].append((T, B))
        adj[T].append((S, B))

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
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    print(dist[N + 1])

if __name__ == "__main__":
    main()
