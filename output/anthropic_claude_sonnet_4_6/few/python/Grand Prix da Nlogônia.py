Looking at this problem, I need to find the minimum X such that accepting plans 1..X creates a directed cycle.

Key insight: Each plan adds edges from U to all vertices in range [L, R]. With N, M up to 2×10^5, I need an efficient approach.

**Approach: Binary search on X + Segment tree for range edges + Cycle detection**

Binary search on X (the answer). For a given X, build the graph with plans 1..X and check if there's a cycle (using DFS/topological sort).

The graph has edges from U to ranges [L,R]. To handle range edges efficiently, I'll use a **segment tree** as auxiliary nodes. The segment tree nodes represent ranges, and:
- Each internal node has edges to its children (so an edge to a segment tree node propagates to all leaves in range)
- Leaf nodes (segment tree) connect to actual graph nodes
- Actual graph nodes connect to segment tree nodes (for range queries)

This gives O(N log N) nodes and O(M log N) edges.

**Segment tree structure:**
- Nodes 1..N: actual vertices
- Nodes N+1..N+4N: segment tree nodes (two trees: one for "source" - actual node to range, one for "sink" - range to actual node)

Actually, standard approach:
- Build a "down" segment tree where parent → children, leaves connect to real nodes
- Build an "up" segment tree where real nodes → leaves, children → parent
- Edge U→[L,R]: U connects to the down-tree node covering [L,R]
- Down-tree leaves connect to real nodes

Let me implement this:

- Real nodes: 0..N-1
- Down seg tree (for range targets): N..N+4N-1, parent→child edges, leaf→real node
- Up seg tree (for range sources): N+4N..N+8N-1, real node→leaf, child→parent edges

For plan (U, L, R): add edge from real node U-1 to down-tree covering [L-1, R-1].

Cycle detection via iterative DFS with coloring (white=0, gray=1, black=2).

Binary search: check if cycle exists with first X plans.

```python
import sys
from sys import setrecursionlimit

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    plans = []
    for _ in range(M):
        u = int(data[idx])-1; idx+=1
        l = int(data[idx])-1; idx+=1
        r = int(data[idx])-1; idx+=1
        plans.append((u,l,r))
    
    SIZE = 4*N
    # Total nodes: N real + SIZE down_tree + SIZE up_tree
    TOTAL = N + 2*SIZE
    DOWN = N  # down tree offset
    UP = N + SIZE  # up tree offset
    
    # Precompute static edges (segment tree structure)
    static_edges = [[] for _ in range(TOTAL)]
    # Down tree: parent -> children, leaf -> real node
    def build_down(node, s, e):
        if s == e:
            static_edges[DOWN+node].append(s)  # leaf to real
            return
        mid = (s+e)//2
        static_edges[DOWN+node].append(DOWN+2*node)
        static_edges[DOWN+node].append(DOWN+2*node+1)
        build_down(2*node, s, mid)
        build_down(2*node+1, mid+1, e)
    # Up tree: real node -> leaf, children -> parent
    def build_up(node, s, e):
        if s == e:
            static_edges[s].append(UP+node)  # real to leaf
            return
        mid = (s+e)//2
        static_edges[UP+2*node].append(UP+node)
        static_edges[UP+2*node+1].append(UP+node)
        build_up(2*node, s, mid)
        build_up(2*node+1, mid+1, e)
    
    sys.setrecursionlimit(300000)
    build_down(1, 0, N-1)
    build_up(1, 0, N-1)
```

Given recursion depth issues with N=200000, let me implement iteratively. Let me write the full solution:

import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    plans = []
    for _ in range(M):
        u = int(data[idx])-1; idx+=1
        l = int(data[idx])-1; idx+=1
        r = int(data[idx])-1; idx+=1
        plans.append((u,l,r))

    SIZE = 4*(N+1)
    DOWN = N
    UP = N + SIZE
    TOTAL = N + 2*SIZE

    static_adj = [[] for _ in range(TOTAL)]

    def build(node, s, e):
        stack = [(node, s, e)]
        while stack:
            nd, ss, ee = stack.pop()
            if ss == ee:
                static_adj[DOWN+nd].append(ss)
                static_adj[ss].append(UP+nd)
                continue
            mid = (ss+ee)//2
            static_adj[DOWN+nd].append(DOWN+2*nd)
            static_adj[DOWN+nd].append(DOWN+2*nd+1)
            static_adj[UP+2*nd].append(UP+nd)
            static_adj[UP+2*nd+1].append(UP+nd)
            stack.append((2*nd, ss, mid))
            stack.append((2*nd+1, mid+1, ee))

    build(1, 0, N-1)

    def query_down(node, s, e, l, r, edges_list):
        stack = [(node, s, e)]
        while stack:
            nd, ss, ee = stack.pop()
            if l <= ss and ee <= r:
                edges_list.append(DOWN+nd)
                continue
            mid = (ss+ee)//2
            if l <= mid:
                stack.append((2*nd, ss, mid))
            if r > mid:
                stack.append((2*nd+1, mid+1, ee))

    plan_edges = []
    for u, l, r in plans:
        targets = []
        query_down(1, 0, N-1, l, r, targets)
        plan_edges.append((u, targets))

    def has_cycle(num_plans):
        adj = [list(static_adj[i]) for i in range(TOTAL)]
        for i in range(num_plans):
            u, targets = plan_edges[i]
            for t in targets:
                adj[u].append(t)
        
        color = [0]*TOTAL
        for start in range(TOTAL):
            if color[start] != 0:
                continue
            stack = [(start, False)]
            while stack:
                node, leaving = stack.pop()
                if leaving:
                    color[node] = 2
                    continue
                if color[node] == 2:
                    continue
                if color[node] == 1:
                    return True
                color[node] = 1
                stack.append((node, True))
                for nb in adj[node]:
                    if color[nb] == 1:
                        return True
                    if color[nb] == 0:
                        stack.append((nb, False))
        return False

    lo, hi = 1, M
    ans = -1
    if not has_cycle(M):
        print(-1)
        return
    
    while lo <= hi:
        mid = (lo+hi)//2
        if has_cycle(mid):
            ans = mid
            hi = mid-1
        else:
            lo = mid+1
    print(ans)

solve()

Wait, this binary search approach with O(TOTAL + M log N) per check and O(log M) iterations might be too slow. TOTAL ~ 9N, and each check is O(9N + M log N). With log M ~ 17 iterations, total ~ 17 * (9*200000 + 200000*17) ~ 17 * (1.8M + 3.4M) ~ 88M operations. Might be tight but let's try.

But copying adj each time is expensive. Let me optimize by not copying static_adj but building fresh each time.

Actually the bigger issue: copying static_adj (size ~1.8M lists) 17 times is very slow in Python. Let me restructure.

Better: precompute static edges once, and for each binary search step, only add plan edges on top. Use a separate dynamic adjacency.

```python
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    plans = []
    for _ in range(M):
        u = int(data[idx])-1; idx+=1
        l = int(data[idx])-1; idx+=1
        r = int(data[idx])-1; idx+=1
        plans.append((u,l,r))

    SIZE = 4*(N+1)
    DOWN = N
    UP = N + SIZE
    TOTAL = N + 2*SIZE

    static_adj = [[] for _ in range(TOTAL)]

    def build(node, s, e):
        stack = [(node, s, e)]
        while stack:
            nd, ss, ee = stack.pop()
            if ss == ee:
                static_adj[DOWN+nd].append(ss)
                static_adj[ss].append(UP+nd)
                continue
            mid = (ss+ee)//2
            static_adj[DOWN+nd].append(DOWN+2*nd)
            static_adj[DOWN+nd].append(DOWN+2*nd+1)
            static_adj[UP+2*nd].append(UP+nd)
            static_adj[UP+2*nd+1].append(UP+nd)
            stack.append((2*nd, ss, mid))
            stack.append((2*nd+1, mid+1, ee))

    build(1, 0, N-1)

    def query_down(l, r):
        result = []
        stack = [(1, 0, N-1)]
        while stack:
            nd, ss, ee = stack.pop()
            if l <= ss and ee <= r:
                result.append(DOWN+nd)
                continue
            mid = (ss+ee)//2
            if l <= mid:
                stack.append((2*nd, ss, mid))
            if r > mid:
                stack.append((2*nd+1, mid+1, ee))
        return result

    plan_edges = []
    for u, l, r in plans:
        targets = query_down(l, r)
        plan_edges.append((u, targets))

    def has_cycle(num_plans):
        # dynamic_adj[v] = extra edges from plans
        dynamic_adj = [[] for _ in range(TOTAL)]
        for i in range(num_plans):
            u, targets = plan_edges[i]
            dynamic_adj[u].extend(targets)
        
        color = bytearray(TOTAL)  # 0=white,1=gray,2=black
        
        for start in range(TOTAL):
            if color[start] != 0:
                continue
            stack = [(start, False)]
            while stack:
                node, leaving = stack.pop()
                if leaving:
                    color[node] = 2
                    continue
                if color[node] == 2:
                    continue
                if color[node] == 1:
                    return True
                color[node] = 1
                stack.append((node, True))
                for nb in static_adj[node]:
                    if color[nb] == 1:
                        return True
                    if color[nb] == 0:
                        stack.append((nb, False))
                for nb in dynamic_adj[node]:
                    if color[nb] == 1:
                        return True
                    if color[nb] == 0:
                        stack.append((nb, False))
        return False

    if not has_cycle(M):
        print(-1)
        return
    
    lo, hi = 1, M
    ans = M
    while lo <= hi:
        mid = (lo+hi)//2
        if has_cycle(mid):
            ans = mid
            hi = mid-1
        else:
            lo = mid+1
    print(ans)

solve()
```

This should work but Python might be slow. Let me think about the complexity more carefully.

Each `has_cycle` call: O(TOTAL + sum of edges). TOTAL ~ 9N. Static edges ~ O(N log N). Dynamic edges for X plans ~ O(X log N). Total per call ~ O(N log N). With 17 binary search steps: O(17 * N log N) ~ 17 * 200000 * 17 ~ 58M. In Python this might TLE.

But let me also verify correctness with the test cases first, then optimize if needed.

Let me trace test 1:
- N=8, M=6
- Plans: (4,5,7), (2,0,1), (5,1,3), (0,3,4), (7,3,6), (1,2,5) (0-indexed)
- Answer: 4

With plans 1-4 (0-indexed 0-3): edges from 4→[5,6,7], 2→[0,1], 5→[1,2,3], 0→[3,4]
- 0→3,4; 4→5,6,7; 5→1,2,3; 3→... wait 5→3 and 0→3... 
- 0→4→5→3... does 3 go back to 0? No.
- 0→4→5→1,2,3; 0→3; 2→0,1; 
- 0→4→5→2→0: cycle! Yes, that's a cycle with 4 plans.

Good, the logic seems correct.

Let me finalize the code:

```python
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    plans = []
    for _ in range(M):
        u = int(data[idx])-1; idx+=1
        l = int(data[idx])-1; idx+=1
        r = int(data[idx])-1; idx+=1
        plans.append((u,l,r))

    SIZE = 4*(N+1)
    DOWN = N
    UP = N + SIZE
    TOTAL = N + 2*SIZE

    static_adj = [[] for _ in range(TOTAL)]

    stack_build = [(1, 0, N-1)]
    while stack_build:
        nd, ss, ee = stack_build.pop()
        if ss == ee:
            static_adj[DOWN+nd].append(ss)
            static_adj[ss].append(UP+nd)
            continue
        mid = (ss+ee)//2
        static_adj[DOWN+nd].append(DOWN+2*nd)
        static_adj[DOWN+nd].append(DOWN+2*nd+1)
        static_adj[UP+2*nd].append(UP+nd)
        static_adj[UP+2*nd+1].append(UP+nd)
        stack_build.append((2*nd, ss, mid))
        stack_build.append((2*nd+1, mid+1, ee))

    def query_down(l, r):
        result = []
        stack = [(1, 0, N-1)]
        while stack:
            nd, ss, ee = stack.pop()
            if l <= ss and ee <= r:
                result.append(DOWN+nd)
                continue
            mid2 = (ss+ee)//2
            if l <= mid2:
                stack.append((2*nd, ss, mid2))
            if r > mid2:
                stack.append((2*nd+1, mid2+1, ee))
        return result

    plan_edges = []
    for u, l, r in plans:
        targets = query_down(l, r)
        plan_edges.append((u, targets))

    def has_cycle(num_plans):
        dynamic_adj = [[] for _ in range(TOTAL)]
        for i in range(num_plans):
            u, targets = plan_edges[i]
            dynamic_adj[u].extend(targets)
        
        color = bytearray(TOTAL)
        
        for start in range(TOTAL):
            if color[start] != 0:
                continue
            stack = [(start, False)]
            while stack:
                node, leaving = stack.pop()
                if leaving:
                    color[node] = 2
                    continue
                c = color[node]
                if c == 2:
                    continue
                if c == 1:
                    return True
                color[node] = 1
                stack.append((node, True))
                for nb in static_adj[node]:
                    cn = color[nb]
                    if cn == 1:
                        return True
                    if cn == 0:
                        stack.append((nb, False))
                for nb in dynamic_adj[node]:
                    cn = color[nb]
                    if cn == 1:
                        return True
                    if cn == 0:
                        stack.append((nb, False))
        return False

    if not has_cycle(M):
        print(-1)
        return
    
    lo, hi = 1, M
    ans = M
    while lo <= hi:
        mid = (lo+hi)//2
        if has_cycle(mid):
            ans = mid
            hi = mid-1
        else:
            lo = mid+1
    print(ans)

solve()
```

import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    plans = []
    for _ in range(M):
        u = int(data[idx])-1; idx+=1
        l = int(data[idx])-1; idx+=1
        r = int(data[idx])-1; idx+=1
        plans.append((u,l,r))

    SIZE = 4*(N+1)
    DOWN = N
    UP = N + SIZE
    TOTAL = N + 2*SIZE

    static_adj = [[] for _ in range(TOTAL)]

    stack_build = [(1, 0, N-1)]
    while stack_build:
        nd, ss, ee = stack_build.pop()
        if ss == ee:
            static_adj[DOWN+nd].append(ss)
            static_adj[ss].append(UP+nd)
            continue
        mid = (ss+ee)//2
        static_adj[DOWN+nd].append(DOWN+2*nd)
        static_adj[DOWN+nd].append(DOWN+2*nd+1)
        static_adj[UP+2*nd].append(UP+nd)
        static_adj[UP+2*nd+1].append(UP+nd)
        stack_build.append((2*nd, ss, mid))
        stack_build.append((2*nd+1, mid+1, ee))

    def query_down(l, r):
        result = []
        stack = [(1, 0, N-1)]
        while stack:
            nd, ss, ee = stack.pop()
            if l <= ss and ee <= r:
                result.append(DOWN+nd)
                continue
            mid2 = (ss+ee)//2
            if l <= mid2:
                stack.append((2*nd, ss, mid2))
            if r > mid2:
                stack.append((2*nd+1, mid2+1, ee))
        return result

    plan_edges = []
    for u, l, r in plans:
        targets = query_down(l, r)
        plan_edges.append((u, targets))

    def has_cycle(num_plans):
        dynamic_adj = [[] for _ in range(TOTAL)]
        for i in range(num_plans):
            u, targets = plan_edges[i]
            dynamic_adj[u].extend(targets)
        
        color = bytearray(TOTAL)
        
        for start in range(TOTAL):
            if color[start] != 0:
                continue
            stack = [(start, False)]
            while stack:
                node, leaving = stack.pop()
                if leaving:
                    color[node] = 2
                    continue
                c = color[node]
                if c == 2:
                    continue
                if c == 1:
                    return True
                color[node] = 1
                stack.append((node, True))
                for nb in static_adj[node]:
                    cn = color[nb]
                    if cn == 1:
                        return True
                    if cn == 0:
                        stack.append((nb, False))
                for nb in dynamic_adj[node]:
                    cn = color[nb]
                    if cn == 1:
                        return True
                    if cn == 0:
                        stack.append((nb, False))
        return False

    if not has_cycle(M):
        print(-1)
        return
    
    lo, hi = 1, M
    ans = M
    while lo <= hi:
        mid = (lo+hi)//2
        if has_cycle(mid):
            ans = mid
            hi = mid-1
        else:
            lo = mid+1
    print(ans)

solve()