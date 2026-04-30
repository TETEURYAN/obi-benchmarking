
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        A = int(data[idx])
        idx += 1
        B = int(data[idx])
        idx += 1
        C = int(data[idx])
        idx += 1
        adj[A].append((B, C))
        adj[B].append((A, C))

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        current_dist, u = heapq.heappop(heap)
        if u == N:
            break
        if current_dist > dist[u]:
            continue
        for (v, cost) in adj[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(heap, (dist[v], v))

    print(dist[N])

if __name__ == "__main__":
    main()
