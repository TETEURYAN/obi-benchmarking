import heapq
import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    
    P = [0] * (K + 1)
    for i in range(1, K + 1):
        P[i] = int(input_data[idx]); idx += 1
    
    # adjacency list: station -> list of (neighbor, transport_system)
    adj = defaultdict(list)
    
    for _ in range(M):
        v = int(input_data[idx]); idx += 1
        u = int(input_data[idx]); idx += 1
        t = int(input_data[idx]); idx += 1
        adj[v].append((u, t))
        adj[u].append((v, t))
    
    A = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    # State: (cost, station, current_transport_system)
    # current_transport_system = 0 means not in any system
    # When we move along an edge with system t:
    #   - if current system == t: cost += 0 (already in system)
    #   - else: cost += P[t] (enter new system)
    
    # dist[station][system] = min cost to reach station while currently in system
    # system 0 = not in any system (initial state)
    
    INF = float('inf')
    
    # Use dict for dist to save memory
    dist = {}
    
    # Priority queue: (cost, station, system)
    # Start at station A, not in any system (system=0)
    pq = [(0, A, 0)]
    dist[(A, 0)] = 0
    
    while pq:
        cost, u, sys_cur = heapq.heappop(pq)
        
        if u == B:
            print(cost)
            return
        
        key = (u, sys_cur)
        if dist.get(key, INF) < cost:
            continue
        
        for v, t in adj[u]:
            # Moving from u to v using system t
            if sys_cur == t:
                new_cost = cost
            else:
                new_cost = cost + P[t]
            
            new_key = (v, t)
            if new_cost < dist.get(new_key, INF):
                dist[new_key] = new_cost
                heapq.heappush(pq, (new_cost, v, t))
    
    print(-1)

solve()