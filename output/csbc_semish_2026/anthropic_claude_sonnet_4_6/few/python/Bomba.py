import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    E = int(data[idx]); idx+=1
    S = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    
    # adj[u] = list of (v, T) where T=1 means opens at multiples of 3, T=0 means closes at multiples of 3
    adj = [[] for _ in range(N)]
    
    for _ in range(M):
        A = int(data[idx]); idx+=1
        B = int(data[idx]); idx+=1
        T = int(data[idx]); idx+=1
        adj[A].append((B, T))
    
    # State: (time, node)
    # At time t, bus is at node u, wants to traverse edge (u,v,T)
    # The bus enters the street at time t, arrives at v at time t+1
    # But the traffic light: the street has a pedestrian crossing with a semaphore
    # The bus needs to pass through the semaphore. 
    # If T=1: opens at multiples of 3, closes otherwise
    # If T=0: closes at multiples of 3, opens otherwise
    # The bus arrives at the street at time t (leaving rotary u at time t)
    # It takes 1 minute to traverse the street
    # The semaphore must be open when the bus passes through it
    # 
    # When does the bus encounter the semaphore? 
    # The bus enters the street at time t and exits at time t+1.
    # The semaphore is at the end of the street (pedestrian crossing before the next rotary).
    # So the bus hits the semaphore at time t+1? Or at time t?
    # 
    # Let's think: the bus leaves rotary at time t, travels 1 minute, arrives at t+1.
    # The pedestrian crossing (semaphore) is on the street. 
    # If the semaphore is red, the bus must stop -> bomb explodes.
    # So we need the semaphore to be green when the bus passes through it.
    # 
    # The semaphore timing: opens at multiples of 3 (T=1) or closes at multiples of 3 (T=0).
    # "opens at multiples of 3" means: at times 0,3,6,9,... it's green; at 1,2,4,5,7,8,... it's red.
    # "closes at multiples of 3" means: at times 0,3,6,9,... it's red; at 1,2,4,5,7,8,... it's green.
    # 
    # When does the bus pass the semaphore? At time t (when it starts the street) or t+1 (when it arrives)?
    # The problem says the street takes exactly 1 minute. The semaphore is a pedestrian crossing on the street.
    # Most likely the bus encounters the semaphore at the moment it enters the street (time t).
    # Or at time t+1 when it exits.
    # 
    # Let's check with test case 1: answer is 8, bus starts at t=0 at node 5.
    # Path: 5->0 (T=1, opens at mult of 3): at t=0, 0 is mult of 3, T=1 means open -> OK, arrives at 0 at t=1
    # 0->1 (T=0, closes at mult of 3): at t=1, not mult of 3, T=0 means open -> OK, arrives at 1 at t=2
    # 1->2 (T=1): at t=2, not mult of 3, T=1 means closed -> NOT OK
    # 1->2 (T=0): at t=2, not mult of 3, T=0 means open -> OK, arrives at 2 at t=3
    # 2->4 (T=0): at t=3, mult of 3, T=0 means closed -> NOT OK
    # 2->3 (T=1): at t=3, mult of 3, T=1 means open -> OK, arrives at 3 at t=4
    # 3->0 (T=0): at t=4, not mult of 3, T=0 means open -> OK, arrives at 0 at t=5
    # 0->1 (T=0): at t=5, not mult of 3, T=0 means open -> OK, arrives at 1 at t=6
    # 1->2 (T=0): at t=6, mult of 3, T=0 means closed -> NOT OK
    # 1->2 (T=1): at t=6, mult of 3, T=1 means open -> OK, arrives at 2 at t=7
    # 2->4 (T=0): at t=7, not mult of 3, T=0 means open -> OK, arrives at 4 at t=8 -> EXIT! Answer=8 ✓
    
    # So the semaphore is checked at time t (when bus starts traversing the street)
    # T=1: open if t%3==0, closed otherwise
    # T=0: closed if t%3==0, open otherwise
    
    # Since the pattern repeats every 3 minutes, state = (node, time%3)
    # But we want minimum time, so use Dijkstra with state (time, node)
    # Since time can grow, but state space is N*3, we track visited[node][time%3]
    
    INF = float('inf')
    dist = [[INF]*3 for _ in range(N)]
    dist[E][0] = 0  # start at node E at time 0
    
    pq = [(0, E)]
    
    while pq:
        t, u = heapq.heappop(pq)
        
        if u == S:
            print(t)
            return
        
        if t > dist[u][t%3]:
            continue
        
        for (v, T) in adj[u]:
            # Check if semaphore is open at time t
            if T == 1:
                open_now = (t % 3 == 0)
            else:
                open_now = (t % 3 != 0)
            
            if open_now:
                nt = t + 1
                if nt < dist[v][nt%3]:
                    dist[v][nt%3] = nt
                    heapq.heappush(pq, (nt, v))
    
    print('*')

solve()