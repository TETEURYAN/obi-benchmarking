import sys
import heapq

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    K = int(data[idx]); idx+=1
    
    P = [0] * (K + 1)
    for i in range(1, K+1):
        P[i] = int(data[idx]); idx+=1
    
    # Build adjacency list: adj[u] = list of (v, transport_type)
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        v = int(data[idx]); idx+=1
        u = int(data[idx]); idx+=1
        t = int(data[idx]); idx+=1
        adj[v].append((u, t))
        adj[u].append((v, t))
    
    A = int(data[idx]); idx+=1
    B = int(data[idx]); idx+=1
    
    # Dijkstra with state (station, current_transport_system)
    # State: (cost, station, transport_system) where transport_system=0 means not in any system
    # When we move along edge with transport t:
    #   if current system == t: cost += 0 (already in system)
    #   else: cost += P[t] (enter new system)
    # 
    # dist[station][transport] = min cost to be at station using transport t
    # transport=0 means we just arrived and haven't entered any system yet (only valid at start)
    
    # Since K can be up to 100000 and N up to 100000, we can't store dist[N][K] array easily
    # Use dictionaries or think differently
    
    # Key insight: when at station u in system t, we can traverse any edge (u,v,t) for free (same system)
    # or traverse edge (u,v,t2) paying P[t2] to switch
    # 
    # State: (cost, node, current_system)
    # dist[(node, system)] = min cost
    
    # Use defaultdict with infinity
    INF = float('inf')
    
    # dist as dict
    dist = {}
    
    # Priority queue: (cost, node, system)
    # Start at A with no system (system=0), cost=0
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
        
        for (v, t) in adj[u]:
            # To use this edge, we need to be in system t
            if t == sys_cur:
                new_cost = cost
            else:
                new_cost = cost + P[t]
            
            new_key = (v, t)
            if new_cost < dist.get(new_key, INF):
                dist[new_key] = new_cost
                heapq.heappush(pq, (new_cost, v, t))
    
    print(-1)

main()