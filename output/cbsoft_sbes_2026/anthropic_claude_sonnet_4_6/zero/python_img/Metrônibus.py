import heapq
import sys
input = sys.stdin.readline

def solve():
    line = sys.stdin.readline().split()
    N, K1, K2, P = int(line[0]), int(line[1]), int(line[2]), int(line[3])
    
    # Graph: adjacency list
    # Each edge: (neighbor, type) where type 0 = metro, type 1 = bus
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(K1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append((v, 0))
        graph[v].append((u, 0))
    
    for _ in range(K2):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append((v, 1))
        graph[v].append((u, 1))
    
    A, B = map(int, sys.stdin.readline().split())
    
    # State: (cost, node, current_system)
    # current_system: -1 = none (not in any system), 0 = metro, 1 = bus
    # When we move along an edge:
    # - If current_system == edge_type: no cost
    # - Else: pay P (switch or enter system)
    
    # dist[node][system] where system in {0, 1}
    INF = float('inf')
    dist = [[INF, INF] for _ in range(N + 1)]
    
    # Priority queue: (cost, node, system)
    # Start at A with no system (-1), but we need to enter a system to move
    # Actually, let's think of it as: we start at A, not in any system
    # When we take first edge of type t, we pay P and enter system t
    
    # We can model starting state as system = -1 (no system)
    # dist_start[node] for system=-1
    dist_start = [INF] * (N + 1)
    dist_start[A] = 0
    
    # heap: (cost, node, system) system: 0, 1, or 2 (meaning "none/start")
    heap = [(0, A, 2)]  # 2 = no system
    
    # dist array: index 0,1 for metro/bus, index 2 for "no system" (only start)
    dist2 = [[INF, INF, INF] for _ in range(N + 1)]
    dist2[A][2] = 0
    
    while heap:
        cost, node, sys_cur = heapq.heappop(heap)
        
        if cost > dist2[node][sys_cur]:
            continue
        
        if node == B:
            print(cost)
            return
        
        for neighbor, edge_type in graph[node]:
            if sys_cur == edge_type:
                # Same system, no extra cost
                new_cost = cost
            else:
                # Switch system or enter new system
                new_cost = cost + P
            
            if new_cost < dist2[neighbor][edge_type]:
                dist2[neighbor][edge_type] = new_cost
                heapq.heappush(heap, (new_cost, neighbor, edge_type))
    
    # Check if B is reachable
    ans = min(dist2[B][0], dist2[B][1])
    if ans == INF:
        print(-1)
    else:
        print(ans)

solve()