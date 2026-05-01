import sys
import heapq

def main():
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    P = [0] + list(map(int, input().split()))

    station_systems = [[] for _ in range(N + 1)]
    pair_to_id = {}
    next_id = N + 1

    for _ in range(M):
        v, u, t = map(int, input().split())
        key1 = (v, t)
        if key1 not in pair_to_id:
            pair_to_id[key1] = next_id
            station_systems[v].append((t, next_id))
            next_id += 1

        key2 = (u, t)
        if key2 not in pair_to_id:
            pair_to_id[key2] = next_id
            station_systems[u].append((t, next_id))
            next_id += 1

    A, B = map(int, input().split())

    total_nodes = next_id - 1
    adj = [[] for _ in range(total_nodes + 1)]

    for s in range(1, N + 1):
        for t, sid in station_systems[s]:
            cost = P[t]
            adj[s].append((sid, cost))
            adj[sid].append((s, 0))

    # Re-read edges is impossible, so store them first
def solve():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    N = int(next(it))
    M = int(next(it))
    K = int(next(it))

    P = [0] + [int(next(it)) for _ in range(K)]

    station_systems = [[] for _ in range(N + 1)]
    pair_to_id = {}
    edges = []
    next_id = N + 1

    for _ in range(M):
        v = int(next(it))
        u = int(next(it))
        t = int(next(it))
        edges.append((v, u, t))

        key = (v, t)
        if key not in pair_to_id:
            pair_to_id[key] = next_id
            station_systems[v].append((t, next_id))
            next_id += 1

        key = (u, t)
        if key not in pair_to_id:
            pair_to_id[key] = next_id
            station_systems[u].append((t, next_id))
            next_id += 1

    A = int(next(it))
    B = int(next(it))

    total_nodes = next_id - 1
    adj = [[] for _ in range(total_nodes + 1)]

    for s in range(1, N + 1):
        for t, sid in station_systems[s]:
            adj[s].append((sid, P[t]))
            adj[sid].append((s, 0))

    for v, u, t in edges:
        idv = pair_to_id[(v, t)]
        idu = pair_to_id[(u, t)]
        adj[idv].append((idu, 0))
        adj[idu].append((idv, 0))

    INF = 10**30
    dist = [INF] * (total_nodes + 1)
    dist[A] = 0
    pq = [(0, A)]

    while pq:
        d, x = heapq.heappop(pq)
        if d != dist[x]:
            continue
        if x == B:
            print(d)
            return
        for y, w in adj[x]:
            nd = d + w
            if nd < dist[y]:
                dist[y] = nd
                heapq.heappush(pq, (nd, y))

    print(-1)

if __name__ == "__main__":
    solve()
