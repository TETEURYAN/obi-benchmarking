
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        p = int(data[idx + 2])
        adj[u].append((v, p))
        adj[v].append((u, p))
        idx += 3

    s = int(data[idx])

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0
    heap = [(0, s)]

    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v, p in adj[u]:
            if dist[v] > dist[u] + p:
                dist[v] = dist[u] + p
                heapq.heappush(heap, (dist[v], v))

    min_ping = INF
    max_ping = -1
    for i in range(1, n + 1):
        if i == s:
            continue
        if dist[i] < min_ping:
            min_ping = dist[i]
        if dist[i] > max_ping:
            max_ping = dist[i]

    print(max_ping - min_ping)

if __name__ == "__main__":
    main()
