Looking at this problem, I need to find a pair (A, B) where:
1. A ≠ B
2. No existing edge (A, B)
3. Adding edge (A, B) doesn't increase connectivity

The connectivity value is the number of ordered pairs (x, y) where x can reach y.

Key insight: Adding edge (A, B) doesn't change connectivity if and only if B is already reachable from A. Because if B is already reachable from A, then for any node u that can reach A, u can already reach B (through A). And for any node v reachable from B, A can already reach v. So no new pairs are created.

So I need to find a pair (A, B) where:
- A ≠ B
- No direct edge (A, B) exists
- B is already reachable from A

This means I need to find a pair (A, B) where there's a path from A to B but no direct edge.

If such a pair exists, I can find it by looking for any node A that has a path of length ≥ 2 to some node B, where no direct edge (A, B) exists.

Algorithm:
- For each node A, find all nodes reachable from A (via BFS/DFS)
- Check if any reachable node B (B ≠ A) doesn't have a direct edge (A, B)

But with N up to 200,000 and M up to 400,000, doing full BFS for each node is too slow.

Better approach: Find Strongly Connected Components (SCCs). Within an SCC of size ≥ 3, or size ≥ 2 with not all pairs having edges, we can find such a pair. Also in the DAG of SCCs, if there's a path of length ≥ 2 between SCCs, we can find such a pair.

Let me think more carefully:
- Condense the graph into SCCs
- In the condensed DAG, if any SCC has size ≥ 2: within that SCC, every pair is mutually reachable. If the SCC has size ≥ 2 and not all directed edges exist within it, we can find a pair. Actually within an SCC of size k≥2, there's always a cycle, so there exist nodes u,v reachable from each other. If there's no direct edge u→v, we found our answer.
- In the condensed DAG, if there's a path of length ≥ 2 (i.e., u → w → v in DAG), then any node in SCC(u) can reach any node in SCC(v) through SCC(w), but there might not be a direct edge.

Let me implement:
1. Compute SCCs
2. For each SCC of size ≥ 2: check if there exist two nodes u, v in it with no direct edge u→v (since they're in same SCC, u can reach v). If found, output.
3. For the condensed DAG: if any node has a path of length ≥ 2 to another, pick representatives and check.

For step 3: In condensed DAG, if node X has an edge to Y, and Y has an edge to Z, then representative of X can reach representative of Z. If no direct edge between them, output that pair.

import sys
from collections import defaultdict

```python
import sys
input = sys.stdin.readline

def solve():
    from sys import setrecursionlimit
    setrecursionlimit(300000)
    
    N, M = map(int, input().split())
    edges = set()
    adj = [[] for _ in range(N+1)]
    radj = [[] for _ in range(N+1)]
    
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x].append(y)
        radj[y].append(x)
        edges.add((x, y))
    
    # Kosaraju's SCC
    visited = [False] * (N+1)
    order = []
    
    def dfs1(v):
        stack = [(v, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for u in adj[node]:
                    if not visited[u]:
                        stack.append((u, 0))
            else:
                order.append(node)
    
    for i in range(1, N+1):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * (N+1)
    num_scc = 0
    
    def dfs2(v, c):
        stack = [v]
        while stack:
            node = stack.pop()
            if comp[node] != -1:
                continue
            comp[node] = c
            for u in radj[node]:
                if comp[u] == -1:
                    stack.append(u)
    
    for v in reversed(order):
        if comp[v] == -1:
            dfs2(v, num_scc)
            num_scc += 1
    
    scc_nodes = defaultdict(list)
    for i in range(1, N+1):
        scc_nodes[comp[i]].append(i)
    
    # Check within SCCs of size >= 2
    for c, nodes in scc_nodes.items():
        if len(nodes) >= 2:
            node_set = set(nodes)
            for u in nodes:
                adj_set = set(v for v in adj[u] if v in node_set)
                for v in nodes:
                    if v != u and v not in adj_set:
                        print(u, v)
                        return
    
    # Check DAG paths of length >= 2
    dag_adj = defaultdict(set)
    for u in range(1, N+1):
        for v in adj[u]:
            if comp[u] != comp[v]:
                dag_adj[comp[u]].add(comp[v])
    
    rep = {}
    for c, nodes in scc_nodes.items():
        rep[c] = nodes[0]
    
    # For each SCC node in DAG, check if any neighbor's neighbor is not directly connected
    for c in range(num_scc):
        for nb in dag_adj[c]:
            for nb2 in dag_adj[nb]:
                if nb2 != c and nb2 not in dag_adj[c]:
                    u = rep[c]
                    v = rep[nb2]
                    if (u, v) not in edges:
                        print(u, v)
                        return
    
    print(-1)

solve()
```