Looking at this problem carefully:

- We have a railway network where each station is part of **at most one cycle**
- This means the graph is a "cactus graph" (each edge belongs to at most one cycle)
- A train enters station X, travels forward (no reverse), and exits at X
- The train has length T, so the path must be long enough to accommodate the train
- We need the **minimum distance** the train travels

Key insight: The train enters at X, goes forward, and comes back to X without reversing. This means the train must traverse a **cycle** that is reachable from X. The train goes from X to the cycle, around the cycle, and back to X.

The path is: X → (path to cycle entry point) → around cycle → back to X
- Distance = 2 * (distance from X to cycle entry) + cycle length
- The train length T must fit: T ≤ total path length (the train must be able to be fully inside while moving)

Wait, re-reading: the train needs to enter and exit the same station. The minimum path where the train goes forward only and returns to start. This requires a cycle. The train traverses: go to cycle, go around cycle, come back. Total = 2*d + cycle_length where d = distance from X to the nearest point on a cycle.

If X is on a cycle itself, d=0, answer = cycle_length (if T ≤ cycle_length).

The condition for feasibility: T ≤ total_path_length (the train fits in the loop).

Let me verify with test cases:
- Test1: Stations 1,3,4 form a cycle (1-3: 12, 3-4: 7, 1-4: 6, total=25). Station 2 connects to 1 with length 10.
  - Query (2,18): d=10, cycle=25, total=2*10+25=45. T=18≤45. ✓
  - Query (1,10): d=0, cycle=25, total=25. T=10≤25. ✓  
  - Query (4,26): Station 4 is on cycle (len=25). T=26>25. → -1 ✓
  - Query (3,25): d=0, cycle=25. T=25≤25. ✓

Algorithm:
1. Find all cycles in the cactus graph (using DFS)
2. For each station, find the minimum 2*d + cycle_length over all reachable cycles
3. For query (X, T): find min path ≥ T, or -1

Since each station is on at most one cycle, and the graph is a cactus, I'll:
1. Find all cycles and their lengths
2. For each node, compute minimum (2*dist_to_cycle + cycle_len) using BFS/Dijkstra from cycle nodes

import sys
from collections import defaultdict
import heapq

def solve():
    data = sys.stdin.read().split()
    idx = 0
    E = int(data[idx]); idx+=1
    R = int(data[idx]); idx+=1
    
    adj = [[] for _ in range(E+1)]
    for _ in range(R):
        a = int(data[idx]); idx+=1
        b = int(data[idx]); idx+=1
        c = int(data[idx]); idx+=1
        adj[a].append((b,c))
        adj[b].append((a,c))
    
    # Find cycles using DFS, track back edges
    # For cactus: find all cycles
    visited = [False]*(E+1)
    depth = [-1]*(E+1)
    parent = [-1]*(E+1)
    parent_weight = [0]*(E+1)
    cycle_nodes = {}  # node -> cycle_length (minimum cycle length accessible at 0 dist)
    
    # DFS to find cycles
    cycles = []  # list of (set_of_nodes, cycle_length)
    
    # Use iterative DFS
    # ... (full implementation below)

Let me implement this fully:

```python
import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    idx = 0
    E = int(data[idx]); idx+=1
    R = int(data[idx]); idx+=1
    adj = [[] for _ in range(E+1)]
    for _ in range(R):
        a=int(data[idx]);idx+=1
        b=int(data[idx]);idx+=1
        c=int(data[idx]);idx+=1
        adj[a].append((b,c))
        adj[b].append((a,c))
    depth=[-1]*(E+1)
    dist_from_root=[0]*(E+1)
    parent=[-1]*(E+1)
    on_cycle=[False]*(E+1)
    cycle_len_at={}
    stack=[]
    for start in range(1,E+1):
        if depth[start]!=-1:continue
        depth[start]=0
        stack=[(start,-1,0,False)]
        while stack:
            u,p,d,processed=stack.pop()
            if processed:continue
            if depth[u]!=-1 and u!=start:continue
            depth[u]=d
            dist_from_root[u]=d
            stack.append((u,p,d,True))
            for v,w in adj[u]:
                if v==p:continue
                if depth[v]==-1:
                    parent[v]=u
                    depth[v]=d+1
                    dist_from_root[v]=dist_from_root[u]+w
                    stack.append((v,u,d+1,False))
                elif depth[v]<depth[u]:
                    # back edge, cycle found
                    pass
    solve()
```

Let me think more carefully and write a clean solution:

```python
import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    idx = 0
    E = int(data[idx]); idx+=1
    R = int(data[idx]); idx+=1
    adj = [[] for _ in range(E+1)]
    for _ in range(R):
        a=int(data[idx]);idx+=1
        b=int(data[idx]);idx+=1
        c=int(data[idx]);idx+=1
        adj[a].append((b,c))
        adj[b].append((a,c))
    
    # Find cycles via DFS (recursive with sys limit)
    sys.setrecursionlimit(300000)
    color = [0]*(E+1)
    disc = [0]*(E+1)
    dist = [0]*(E+1)  # dist from DFS root
    par = [-1]*(E+1)
    par_w = [0]*(E+1)
    timer = [0]
    
    # cycle_length[v] = length of cycle that v belongs to (if any)
    cycle_length = [0]*(E+1)
    on_cycle = [False]*(E+1)
    
    def dfs(u, p):
        color[u] = 1
        timer[0] += 1
        disc[u] = timer[0]
        for v, w in adj[u]:
            if v == p:
                continue
            if color[v] == 0:
                par[v] = u
                par_w[v] = w
                dist[v] = dist[u] + w
                dfs(v, u)
            elif color[v] == 1 and disc[v] < disc[u]:
                # back edge u->v, cycle
                clen = dist[u] - dist[v] + w
                # mark all nodes on cycle from u back to v
                node = u
                while node != v:
                    on_cycle[node] = True
                    cycle_length[node] = clen
                    node = par[node]
                on_cycle[v] = True
                cycle_length[v] = clen
        color[u] = 2
    
    for i in range(1, E+1):
        if color[i] == 0:
            dist[i] = 0
            dfs(i, -1)
    
    # Now for each node, find minimum (2*d + cycle_len) where d = shortest dist to any cycle node
    # Use multi-source Dijkstra from all cycle nodes with 0 cost, propagating
    # Actually: for each node u, best[u] = min over all cycle nodes c of (2*shortest_path(u,c) + cycle_length[c])
    
    # Since we want minimum, do Dijkstra where we propagate from cycle nodes
    # State: (cost_so_far_as_2d + cycle_len, node)
    # For cycle nodes: initial cost = cycle_length[c], dist_to_cycle = 0
    # When we move from c to neighbor n with edge weight w: new_dist_to_cycle = w, cost = 2*w + cycle_len
    
    INF = float('inf')
    best = [INF]*(E+1)
    
    pq = []
    for v in range(1, E+1):
        if on_cycle[v]:
            best[v] = cycle_length[v]
            heappush(pq, (cycle_length[v], v, 0))  # (best_cost, node, dist_to_cycle)
    
    # Dijkstra: state = (current_best_answer_if_we_stop_here, node, dist_traveled_from_cycle)
    # When we go from node u to neighbor v with weight w:
    # new_dist = dist_to_cycle + w
    # new_cost = cycle_len_source + 2*(dist_to_cycle + w)
    # But we need to track which cycle we came from...
    
    # Alternative: just do Dijkstra for shortest distance from each node to any cycle node
    # Then best[u] = min over cycle nodes c of (2*d(u,c) + cycle_len[c])
    
    # Multi-source: push all cycle nodes with dist=0, find shortest dist to cycle for each node
    # But different cycle nodes have different cycle_lengths, so we can't just do standard multi-source
    
    # We need: for each node u, min_c (2*d(u,c) + cycle_len[c])
    # This is like a modified Dijkstra where each "source" has a different base cost
    
    # Push (cycle_len[c], c) for all cycle nodes c
    # When relaxing edge (u,v,w): new_val = best[u] + 2*w (since going one more step adds 2*w to round trip)
    
    best2 = [INF]*(E+1)
    pq2 = []
    for v in range(1, E+1):
        if on_cycle[v]:
            best2[v] = cycle_length[v]
            heappush(pq2, (cycle_length[v], v))
    
    while pq2:
        d, u = heappop(pq2)
        if d > best2[u]:
            continue
        for v, w in adj[u]:
            nd = d + 2*w
            if nd < best2[v]:
                best2[v] = nd
                heappush(pq2, (nd, v))
    
    K = int(data[idx]); idx+=1
    out = []
    for _ in range(K):
        X = int(data[idx]); idx+=1
        T = int(data[idx]); idx+=1
        ans = best2[X]
        if ans == INF or T > ans:
            out.append('-1')
        else:
            out.append(str(ans))
    print('\n'.join(out))

solve()
```

Wait, I need to verify the Dijkstra propagation. If a node u has best2[u] = cycle_len + 2*d(u, cycle), and we go to neighbor v with edge w, then best2[v] ≤ cycle_len + 2*(d(u,cycle) + w) = best2[u] + 2*w. Yes, that's correct!

But there's an issue with the DFS for finding cycles - I need to handle the parent edge carefully (multigraph not possible per constraints, but need to handle undirected properly).

Also the DFS might have issues with the parent tracking in undirected graphs. Let me be more careful:

```python
import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    idx = 0
    E = int(data[idx]); idx+=1
    R = int(data[idx]); idx+=1
    adj = [[] for _ in range(E+1)]
    for _ in range(R):
        a=int(data[idx]);idx+=1
        b=int(data[idx]);idx+=1
        c=int(data[idx]);idx+=1
        adj[a].append((b,c))
        adj[b].append((a,c))
    
    sys.setrecursionlimit(300000)
    color = [0]*(E+1)
    disc = [-1]*(E+1)
    dist = [0]*(E+1)
    par = [-1]*(E+1)
    par_w = [0]*(E+1)
    timer = [0]
    on_cycle = [False]*(E+1)
    cycle_length = [0]*(E+1)
    
    def dfs(u, p):
        color[u] = 1
        timer[0] += 1
        disc[u] = timer[0]
        for v, w in adj[u]:
            if v == p:
                continue
            if color[v] == 0:
                par[v] = u
                par_w[v] = w
                dist[v] = dist[u] + w
                dfs(v, u)
            elif color[v] == 1:
                # back edge, found cycle
                clen = dist[u] - dist[v] + w
                node = u
                while node != v:
                    on_cycle[node] = True
                    cycle_length[node] = clen
                    node = par[node]
                on_cycle[v] = True
                cycle_length[v] = clen
        color[u] = 2
    
    for i in range(1, E+1):
        if color[i] == 0:
            dfs(i, -1)
    
    INF = float('inf')
    best = [INF]*(E+1)
    pq = []
    for v in range(1, E+1):
        if on_cycle[v]:
            best[v] = cycle_length[v]
            heappush(pq, (cycle_length[v], v))
    
    while pq:
        d, u = heappop(pq)
        if d > best[u]:
            continue
        for v, w in adj[u]:
            nd = d + 2*w
            if nd < best[v]:
                best[v] = nd
                heappush(pq, (nd, v))
    
    K = int(data[idx]); idx+=1
    out = []
    for _ in range(K):
        X = int(data[idx]); idx+=1
        T = int(data[idx]); idx+=1
        ans = best[X]
        if ans == INF or T > ans:
            out.append('-1')
        else:
            out.append(str(ans))
    print('\n'.join(out))

solve()
```

Let me trace through test case 1:
- Edges: 1-2(10), 1-3(12), 3-4(7), 1-4(6)
- Cycle: 1-3-4-1, length = 12+7+6 = 25
- on_cycle: 1,3,4 = True, cycle_length = 25
- best[1]=25, best[3]=25, best[4]=25
- Dijkstra: from node 2 (neighbor of 1 with w=10): best[2] = 25 + 2*10 = 45

Queries:
- (2,18): best[2]=45, T=18≤45 → 45 ✓
- (1,10): best[1]=25, T=10≤25 → 25 ✓
- (4,26): best[4]=25, T=26>25 → -1 ✓
- (3,25): best[3]=25, T=25≤25 → 25 ✓

Test case 2:
- Edges: 1-2(2), 2-3(2), 2-5(10), 5-6(25), 2-6(20), 3-7(1), 4-7(4), 3-4(3)
- Cycles: 2-5-6-2 (10+25+20=55), 3-7-4-3 (1+4+3=8)
- on_cycle: 2,5,6 with len=55; 3,7,4 with len=8

best values:
- best[2]=55, best[5]=55, best[6]=55
- best[3]=8, best[7]=8, best[4]=8
- From 2's neighbors: 1(w=2): best[1]=55+4=59? But also from 3(w=2): best[1] via 2... wait
  - Actually from node 2: neighbor 1 with w=2: best[1] = min(INF, 55+4) = 59
  - From node 3: neighbor 2 with w=2: best[2] = min(55, 8+4) = 12
  
Hmm! Node 2 is on cycle (2-5-6-2, len=55), but it's also reachable from cycle (3-7-4-3, len=8) via edge 2-3(w=2). So best[2] should be min(55, 8+2*2) = min(55,12) = 12.

Let me re-trace Dijkstra:
Initial: best[2]=55, best[5]=55, best[6]=55, best[3]=8, best[7]=8, best[4]=8
PQ: [(8,3),(8,4),(8,7),(55,2),(55,5),(55,6)]

Pop (8,3): neighbors: 2(w=2)->nd=12<55, update best[2]=12; 7(w=1)->nd=10>8 no; 4(w=3)->nd=14>8 no
Pop (8,4): neighbors: 7(w=4)->nd=16>8 no; 3(w=3)->nd=14>8 no
Pop (8,7): neighbors: 3(w=1)->nd=10>8 no; 4(w=4)->nd=16>8 no
Pop (12,2): neighbors: 1(w=2)->nd=16, best[1]=16; 3(w=2)->nd=16>8 no; 5(w=10)->nd=32<55, best[5]=32; 6(w=20)->nd=52<55, best[6]=52
Pop (16,1): no unvisited neighbors improve
Pop (32,5): neighbors: 2(w=10)->nd=52>12 no; 6(w=25)->nd=82>52 no
Pop (52,6): neighbors: 5(w=25)->nd=102>32 no; 2(w=20)->nd=92>12 no
Pop (55,2): d=55>best[2]=12, skip
...

Final best: [INF, 16, 12, 8, 8, 32, 52, 8]

Queries:
- (1,6): best[1]=16, T=6≤16 → 16 ✓
- (4,50): best[4]=8, T=50>8 → -1 ✓
- (7,56): best[7]=8, T=56>8 → -1 ✓
- (7,5): best[7]=8, T=5≤8 → 8 ✓

All correct! The solution works. But I need to handle the DFS carefully for the parent edge in undirected graphs. The issue is when there are multiple edges - but the problem says at most one edge between two stations, so tracking parent by node ID is fine.

However, there's still a subtle issue: in undirected DFS, when we see a visited node v with color=1, it could be the parent (we should skip it). I'm already skipping `v == p`, but what if there are multiple edges? The problem says no multiple edges, so we're fine.

But wait - what if the graph has multiple components? The DFS handles that with the outer loop.

Also, recursion depth could be E=10^4, which is fine with limit 300000.

One more issue: in the DFS, when I find a back edge to an already-gray node, I need to make sure I'm not double-counting cycles. Since each station is on at most one cycle, this should be fine.

The solution looks correct. Let me write the final clean version:

```python
import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    idx = 0
    E = int(data[idx]); idx+=1
    R = int(data[idx]); idx+=1
    adj = [[] for _ in range(E+1)]
    for _ in range(R):
        a=int(data[idx]);idx+=1
        b=int(data[idx]);idx+=1
        c=int(data[idx]);idx+=1
        adj[a].append((b,c))
        adj[b].append((a,c))
    
    sys.setrecursionlimit(300000)
    color = [0]*(E+1)
    disc = [-1]*(E+1)
    dist = [0]*(E+1)
    par = [-1]*(E+1)
    timer = [0]
    on_cycle = [False]*(E+1)
    cycle_length = [0]*(E+1)
    
    def dfs(u, p):
        color[u] = 1
        timer[0] += 1
        disc[u] = timer[0]
        for v, w in adj[u]:
            if v == p:
                continue
            if color[v] == 0:
                par[v] = u
                dist[v] = dist[u] + w
                dfs(v, u)
            elif color[v] == 1:
                clen = dist[u] - dist[v] + w
                node = u
                while node != v:
                    on_cycle[node] = True
                    cycle_length[node] = clen
                    node = par[node]
                on_cycle[v] = True
                cycle_length[v] = clen
        color[u] = 2
    
    for i in range(1, E+1):
        if color[i] == 0:
            dfs(i, -1)
    
    INF = float('inf')
    best = [INF]*(E+1)
    pq = []
    for v in range(1, E+1):
        if on_cycle[v]:
            best[v] = cycle_length[v]
            heappush(pq, (cycle_length[v], v))
    
    while pq:
        d, u = heappop(pq)
        if d > best[u]:
            continue
        for v, w in adj[u]:
            nd = d + 2*w
            if nd < best[v]:
                best[v] = nd
                heappush(pq, (nd, v))
    
    K = int(data[idx]); idx+=1
    out = []
    for _ in range(K):
        X = int(data[idx]); idx+=1
        T = int(data[idx]); idx+=1
        ans = best[X]
        if ans == INF or T > ans:
            out.append('-1')
        else:
            out.append(str(ans))
    print('\n'.join(out))

solve()
```

This should be the correct solution. Let me also consider edge cases:
- Station with no cycle reachable: best = INF → output -1
- Train length exactly equals cycle length: valid
- Station on cycle but train too long: -1

The solution handles all these correctly.

import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    idx = 0
    E = int(data[idx]); idx+=1
    R = int(data[idx]); idx+=1
    adj = [[] for _ in range(E+1)]
    for _ in range(R):
        a=int(data[idx]);idx+=1
        b=int(data[idx]);idx+=1
        c=int(data[idx]);idx+=1
        adj[a].append((b,c))
        adj[b].append((a,c))
    
    sys.setrecursionlimit(300000)
    color = [0]*(E+1)
    dist = [0]*(E+1)
    par = [-1]*(E+1)
    timer = [0]
    on_cycle = [False]*(E+1)
    cycle_length = [0]*(E+1)
    
    def dfs(u, p):
        color[u] = 1
        timer[0] += 1
        for v, w in adj[u]:
            if v == p:
                continue
            if color[v] == 0:
                par[v] = u
                dist[v] = dist[u] + w
                dfs(v, u)
            elif color[v] == 1:
                clen = dist[u] - dist[v] + w
                node = u
                while node != v:
                    on_cycle[node] = True
                    cycle_length[node] = clen
                    node = par[node]
                on_cycle[v] = True
                cycle_length[v] = clen
        color[u] = 2
    
    for i in range(1, E+1):
        if color[i] == 0:
            dfs(i, -1)
    
    INF = float('inf')
    best = [INF]*(E+1)
    pq = []
    for v in range(1, E+1):
        if on_cycle[v]:
            best[v] = cycle_length[v]
            heappush(pq, (cycle_length[v], v))
    
    while pq:
        d, u = heappop(pq)
        if d > best[u]:
            continue
        for v, w in adj[u]:
            nd = d + 2*w
            if nd < best[v]:
                best[v] = nd
                heappush(pq, (nd, v))
    
    K = int(data[idx]); idx+=1
    out = []
    for _ in range(K):
        X = int(data[idx]); idx+=1
        T = int(data[idx]); idx+=1
        ans = best[X]
        if ans == INF or T > ans:
            out.append('-1')
        else:
            out.append(str(ans))
    print('\n'.join(out))

solve()