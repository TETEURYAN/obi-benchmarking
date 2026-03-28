import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx]); idx += 1
    K1 = int(data[idx]); idx += 1
    K2 = int(data[idx]); idx += 1
    P = int(data[idx]); idx += 1

    adj_metro = [[] for _ in range(N + 1)]
    adj_onibus = [[] for _ in range(N + 1)]

    for _ in range(K1):
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        adj_metro[u].append(v)
        adj_metro[v].append(u)

    for _ in range(K2):
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        adj_onibus[u].append(v)
        adj_onibus[v].append(u)

    A = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1

    # Dijkstra com duas "cores" (0 = metro, 1 = onibus)
    INF = 10**18
    dist = [[INF, INF] for _ in range(N + 1)]
    dist[A][0] = 0
    dist[A][1] = 0

    pq = []
    heapq = []
    heapq.append((0, A, 0))
    heapq.append((0, A, 1))

    while heapq:
        d, u, tipo = heapq.pop(0)
        if d > dist[u][tipo]:
            continue

        # Mesmo sistema
        lista = adj_metro if tipo == 0 else adj_onibus
        for v in lista[u]:
            nd = d
            if nd < dist[v][tipo]:
                dist[v][tipo] = nd
                heapq.append((nd, v, tipo))

        # Trocar sistema (paga passagem)
        outro_tipo = 1 - tipo
        nd = d + P
        if nd < dist[u][outro_tipo]:
            dist[u][outro_tipo] = nd
            heapq.append((nd, u, outro_tipo))

    ans = min(dist[B][0], dist[B][1])
    print(ans if ans < INF else -1)

if __name__ == "__main__":
    main()