import sys
import heapq

def main():
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    P = [0] + list(map(int, input().split()))

    station_systems = [[] for _ in range(N + 1)]
    edges = []

    for _ in range(M):
        v, u, t = map(int, input().split())
        edges.append((v, u, t))
        station_systems[v].append(t)
        station_systems[u].append(t)

    A, B = map(int, input().split())

    if A == B:
        print(0)
        return

    pair_to_id = {}
    next_id = N + 1

    for s in range(1, N + 1):
        if station_systems[s]:
            station_systems[s].sort()
            uniq = []
            prev = -1
            for t in station_systems[s]:
                if t != prev:
                    uniq.append(t)
                    prev = t
            station_systems[s] = uniq
            for t in uniq:
                pair_to_id[(s, t)] = next_id
                next_id += 1

    total_nodes = next_id - 1
    adj = [[] for _ in range(total_nodes + 1)]

    for s in range(1, N + 1):
        for t in station_systems[s]:
            pid = pair_to_id[(s, t)]
            cost = P[t]
            adj[s].append((pid, cost))
            adj[pid].append((s, 0))

    for v, u, t in edges:
        id1 = pair_to_id[(v, t)]
        id2 = pair_to_id[(u, t)]
        adj[id1].append((id2, 0))
        adj[id2].append((id1, 0))

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
    main()
