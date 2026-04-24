import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    total_vertices = n + 2
    adj = [[] for _ in range(total_vertices)]
    for _ in range(m):
        s = int(next(it))
        t = int(next(it))
        b = int(next(it))
        adj[s].append((t, b))
        adj[t].append((s, b))
    
    INF = 10**18
    dist = [INF] * total_vertices
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        if u == n + 1:
            print(d)
            return
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    print(dist[n + 1])

if __name__ == "__main__":
    main()