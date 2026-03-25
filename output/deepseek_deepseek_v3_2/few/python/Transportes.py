import sys
import heapq

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    price = [0] * (K + 1)
    for i in range(1, K + 1):
        price[i] = int(next(it))
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        t = int(next(it))
        adj[u].append((v, t))
        adj[v].append((u, t))
    A = int(next(it))
    B = int(next(it))

    INF = 10**18
    dist = [[INF] * (K + 1) for _ in range(N + 1)]
    pq = []
    for t in range(1, K + 1):
        dist[A][t] = price[t]
        heapq.heappush(pq, (price[t], A, t))
    while pq:
        d, u, cur_sys = heapq.heappop(pq)
        if d > dist[u][cur_sys]:
            continue
        if u == B:
            print(d)
            return
        for v, edge_sys in adj[u]:
            new_cost = d
            if edge_sys != cur_sys:
                new_cost += price[edge_sys]
            if new_cost < dist[v][edge_sys]:
                dist[v][edge_sys] = new_cost
                heapq.heappush(pq, (new_cost, v, edge_sys))
    ans = min(dist[B])
    print(ans if ans < INF else -1)

if __name__ == "__main__":
    solve()