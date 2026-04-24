import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    K1 = int(data[idx]); idx+=1
    K2 = int(data[idx]); idx+=1
    P = int(data[idx]); idx+=1
    
    # Metro edges (system 0), Bus edges (system 1)
    metro = [[] for _ in range(N+1)]
    bus = [[] for _ in range(N+1)]
    
    for _ in range(K1):
        u = int(data[idx]); idx+=1
        v = int(data[idx]); idx+=1
        metro[u].append(v)
        metro[v].append(u)
    
    for _ in range(K2):
        u = int(data[idx]); idx+=1
        v = int(data[idx]); idx+=1
        bus[u].append(v)
        bus[v].append(u)
    
    A = int(data[idx]); idx+=1
    B = int(data[idx]); idx+=1
    
    # State: (cost, node, system)
    # system: 0 = metro, 1 = bus, 2 = not in any system (initial)
    # We model it as: node in system 0, node in system 1
    # To enter a system costs P
    # Moving within same system costs 0
    # Switching systems costs P (pay to enter new system)
    
    # dist[node][system]: 0=metro, 1=bus
    INF = float('inf')
    dist = [[INF, INF] for _ in range(N+1)]
    
    # Priority queue: (cost, node, system)
    # Start at A, not in any system. To enter metro: cost P, to enter bus: cost P
    pq = []
    
    # Enter metro at A
    heapq.heappush(pq, (P, A, 0))
    # Enter bus at A
    heapq.heappush(pq, (P, A, 1))
    
    dist[A][0] = P
    dist[A][1] = P
    
    while pq:
        cost, node, sys_type = heapq.heappop(pq)
        
        if cost > dist[node][sys_type]:
            continue
        
        if node == B:
            print(cost)
            return
        
        # Move within same system (cost 0)
        if sys_type == 0:
            neighbors = metro[node]
        else:
            neighbors = bus[node]
        
        for nb in neighbors:
            new_cost = cost
            if new_cost < dist[nb][sys_type]:
                dist[nb][sys_type] = new_cost
                heapq.heappush(pq, (new_cost, nb, sys_type))
        
        # Switch system: pay P to enter the other system at current node
        other = 1 - sys_type
        new_cost = cost + P
        if new_cost < dist[node][other]:
            dist[node][other] = new_cost
            heapq.heappush(pq, (new_cost, node, other))
    
    # Check if B is reachable
    ans = min(dist[B][0], dist[B][1])
    if ans == INF:
        print(-1)
    else:
        print(ans)

solve()