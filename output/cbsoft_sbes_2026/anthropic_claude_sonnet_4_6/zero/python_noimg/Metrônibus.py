import heapq
import sys
input = sys.stdin.readline

def solve():
    line = sys.stdin.readline().split()
    N, K1, K2, P = int(line[0]), int(line[1]), int(line[2]), int(line[3])
    
    # metro edges (type 0), bus edges (type 1)
    metro = [[] for _ in range(N + 1)]
    bus = [[] for _ in range(N + 1)]
    
    for _ in range(K1):
        v, u = map(int, sys.stdin.readline().split())
        metro[v].append(u)
        metro[u].append(v)
    
    for _ in range(K2):
        x, y = map(int, sys.stdin.readline().split())
        bus[x].append(y)
        bus[y].append(x)
    
    A, B = map(int, sys.stdin.readline().split())
    
    # State: (cost, node, current_system)
    # current_system: 0 = metro, 1 = bus, 2 = none (not in any system)
    # When we move along an edge of type t:
    #   if current_system == t: no cost
    #   else: pay P, switch to system t
    
    # dist[node][system] where system in {0, 1, 2}
    INF = float('inf')
    dist = [[INF, INF, INF] for _ in range(N + 1)]
    
    # Start at A with no system (state 2)
    dist[A][2] = 0
    
    # Priority queue: (cost, node, system)
    pq = [(0, A, 2)]
    
    while pq:
        cost, node, sys_cur = heapq.heappop(pq)
        
        if cost > dist[node][sys_cur]:
            continue
        
        if node == B:
            print(cost)
            return
        
        # Try metro edges (type 0)
        for nb in metro[node]:
            if sys_cur == 0:
                new_cost = cost
                new_sys = 0
            else:
                new_cost = cost + P
                new_sys = 0
            if new_cost < dist[nb][new_sys]:
                dist[nb][new_sys] = new_cost
                heapq.heappush(pq, (new_cost, nb, new_sys))
        
        # Try bus edges (type 1)
        for nb in bus[node]:
            if sys_cur == 1:
                new_cost = cost
                new_sys = 1
            else:
                new_cost = cost + P
                new_sys = 1
            if new_cost < dist[nb][new_sys]:
                dist[nb][new_sys] = new_cost
                heapq.heappush(pq, (new_cost, nb, new_sys))
    
    # Check if B is reachable
    ans = min(dist[B][0], dist[B][1], dist[B][2])
    if ans == INF:
        print(-1)
    else:
        print(ans)

solve()