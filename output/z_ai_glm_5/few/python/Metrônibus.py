import sys
import heapq

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        K1 = int(next(iterator))
        K2 = int(next(iterator))
        P = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list: adj[u] stores list of (v, type)
    # type 0 = Subway (Trilho), type 1 = Bus (Rodovia)
    adj = [[] for _ in range(N + 1)]

    # Read Subway edges
    for _ in range(K1):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append((v, 0))
        adj[v].append((u, 0))

    # Read Bus edges
    for _ in range(K2):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append((v, 1))
        adj[v].append((u, 1))

    A = int(next(iterator))
    B = int(next(iterator))

    # Dijkstra's Algorithm
    # dist[u][t] stores the minimum cost to reach station u while inside system t (0 or 1)
    # Initialize with infinity
    inf = float('inf')
    dist = [[inf, inf] for _ in range(N + 1)]
    
    # Priority Queue: (cost, node, system_type)
    pq = []
    
    # Initial state: We are at A. To move, we must enter a system.
    # We can enter either system 0 or 1, paying P.
    # We push both possibilities to the PQ.
    dist[A][0] = P
    dist[A][1] = P
    heapq.heappush(pq, (P, A, 0))
    heapq.heappush(pq, (P, A, 1))
    
    while pq:
        d, u, t = heapq.heappop(pq)
        
        # If we found a better way to this state, skip
        if d > dist[u][t]:
            continue
        
        # If we reached B, this is the minimum cost due to Dijkstra's property
        if u == B:
            print(d)
            return

        # Explore neighbors
        for v, edge_type in adj[u]:
            if edge_type == t:
                # Same system: cost 0 to move
                if dist[v][t] > d:
                    dist[v][t] = d
                    heapq.heappush(pq, (d, v, t))
            else:
                # Different system: must pay P to enter the new system
                new_d = d + P
                if dist[v][edge_type] > new_d:
                    dist[v][edge_type] = new_d
                    heapq.heappush(pq, (new_d, v, edge_type))
    
    # If queue empty and B not reached
    print(-1)

if __name__ == '__main__':
    solve()