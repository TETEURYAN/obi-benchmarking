
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    graph = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        c = int(data[index + 2])
        graph[a].append((b, c))
        graph[b].append((a, c))
        index += 3

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0

    import heapq
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        current_dist, u = heapq.heappop(heap)
        if u == n:
            break
        if current_dist > dist[u]:
            continue
        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(heap, (dist[v], v))

    print(dist[n])

if __name__ == "__main__":
    main()
