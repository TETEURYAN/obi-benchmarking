import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = int(data[0])
    M = int(data[1])
    
    adj = [[] for _ in range(N + 2)]  # 0..N+1
    
    idx = 2
    for _ in range(M):
        S = int(data[idx])
        T = int(data[idx + 1])
        B = int(data[idx + 2])
        adj[S].append((T, B))
        adj[T].append((S, B))
        idx += 3
    
    # Dijkstra
    INF = 10**9
    dist = [INF] * (N + 2)
    dist[0] = 0
    pq = [(0, 0)]  # (holes, pillar)
    
    while pq:
        holes, u = heapq.heappop(pq)
        if holes > dist[u]:
            continue
        if u == N + 1:
            print(holes)
            return
        for v, b in adj[u]:
            new_holes = holes + b
            if new_holes < dist[v]:
                dist[v] = new_holes
                heapq.heappush(pq, (new_holes, v))
    
    # Se chegou aqui, o caminho existe (garantido pelo problema)
    print(dist[N + 1])

if __name__ == "__main__":
    main()