import sys
from collections import deque
input = sys.stdin.readline

def solve():
    N = int(input())
    F = list(map(int, input().split()))
    # F[i] is destination of city i+1 (0-indexed: F[i] is 1-indexed)
    
    # Build next array (1-indexed)
    nxt = [0] * (N + 1)
    for i in range(N):
        nxt[i+1] = F[i]
    
    # Find the cycle using Floyd or coloring
    # Since each node has exactly one outgoing edge, we have a functional graph
    # with exactly one cycle
    
    # Find cycle nodes
    visited = [0] * (N + 1)  # 0: unvisited, 1: in progress, 2: done
    on_cycle = [False] * (N + 1)
    
    # Find cycle by following paths
    # Use the standard approach for functional graphs
    color = [0] * (N + 1)
    cycle_nodes = []
    
    for start in range(1, N + 1):
        if color[start] == 0:
            path = []
            node = start
            while color[node] == 0:
                color[node] = 1
                path.append(node)
                node = nxt[node]
            if color[node] == 1:
                # Found cycle
                idx = path.index(node)
                for cn in path[idx:]:
                    on_cycle[cn] = True
                    cycle_nodes.append(cn)
            for p in path:
                color[p] = 2
    
    # Build cycle order and positions
    # Find cycle order: start from cycle_nodes[0], follow nxt
    cycle_start = cycle_nodes[0]
    cycle_order = [cycle_start]
    cur = nxt[cycle_start]
    while cur != cycle_start:
        cycle_order.append(cur)
        cur = nxt[cur]
    
    cycle_len = len(cycle_order)
    cycle_pos = {}
    for i, cn in enumerate(cycle_order):
        cycle_pos[cn] = i
    
    # For each node, compute:
    # - dist_to_cycle[v]: distance from v to the cycle entry point
    # - cycle_entry[v]: which cycle node v enters
    
    dist_to_cycle = [0] * (N + 1)
    cycle_entry = [0] * (N + 1)
    
    for cn in cycle_order:
        dist_to_cycle[cn] = 0
        cycle_entry[cn] = cn
    
    # BFS/DFS from cycle nodes backwards? 
    # Actually we need to go forward: for non-cycle nodes, follow nxt until cycle
    # Use memoization
    
    memo_dist = [-1] * (N + 1)
    memo_entry = [0] * (N + 1)
    
    for cn in cycle_order:
        memo_dist[cn] = 0
        memo_entry[cn] = cn
    
    def get_dist_entry(v):
        if memo_dist[v] != -1:
            return memo_dist[v], memo_entry[v]
        path = []
        node = v
        while memo_dist[node] == -1:
            path.append(node)
            node = nxt[node]
        d, e = memo_dist[node], memo_entry[node]
        for p in reversed(path):
            d += 1
            memo_dist[p] = d
            memo_entry[p] = e
        # Fix: we need to recompute properly
        # Actually let's redo
        return memo_dist[v], memo_entry[v]
    
    # Recompute properly
    memo_dist = [-1] * (N + 1)
    memo_entry = [0] * (N + 1)
    for cn in cycle_order:
        memo_dist[cn] = 0
        memo_entry[cn] = cn
    
    for v in range(1, N + 1):
        if memo_dist[v] == -1:
            path = []
            node = v
            while memo_dist[node] == -1:
                path.append(node)
                node = nxt[node]
            base_d = memo_dist[node]
            base_e = memo_entry[node]
            for p in reversed(path):
                base_d += 1
                memo_dist[p] = base_d
                memo_entry[p] = base_e
    
    Q = int(input())
    out = []
    
    for _ in range(Q):
        A, B = map(int, input().split())
        if A == B:
            out.append(0)
            continue
        
        dA = memo_dist[A]
        dB = memo_dist[B]
        eA = memo_entry[A]
        eB = memo_entry[B]
        
        if eA == eB:
            # Same entry point, meet before or at cycle
            out.append(abs(dA - dB))
        else:
            # Different entry points
            # They reach cycle at positions cycle_pos[eA] and cycle_pos[eB]
            pA = cycle_pos[eA]
            pB = cycle_pos[eB]
            
            # Option: A waits, B walks to eA: cost = max(dA, dB + dist(eB->eA))
            # dist on cycle from pB to pA (clockwise)
            def cycle_dist(frm, to):
                return (to - frm) % cycle_len
            
            dBA = cycle_dist(pB, pA)
            dAB = cycle_dist(pA, pB)
            
            # Meet at eA: time = max(dA, dB + dBA)
            # Meet at eB: time = max(dB, dA + dAB)
            # Meet somewhere on cycle between eA and eB
            # Best meeting on cycle: minimize max(dA + x, dB + y) where x+y = dAB or dBA
            
            best = float('inf')
            # Direction A->B (A moves dAB steps, B moves 0): max(dA+dAB, dB) but B can also move
            # Actually minimize over meeting point on cycle
            # Going A towards B direction: A travels x steps (0<=x<=dAB), B travels dAB-x steps
            # time = max(dA+x, dB+(dAB-x))
            # optimal x: dA+x = dB+dAB-x => x=(dB+dAB-dA)/2
            for dist_dir in [dAB, dBA]:
                # A goes dist_dir to reach B's entry (or B goes dist_dir to reach A's entry)
                # Actually: one direction A travels x, B travels dist_dir - x
                # Swap roles for other direction
                pass
            
            # Direction 1: A moves toward B (distance dAB on cycle)
            x_opt = (dB + dAB - dA) / 2.0
            x_opt = max(0, min(dAB, x_opt))
            for x in [int(x_opt), int(x_opt)+1]:
                x = max(0, min(dAB, x))
                t = max(dA + x, dB + (dAB - x))
                best = min(best, t)
            
            # Direction 2: B moves toward A (distance dBA on cycle)
            x_opt2 = (dA + dBA - dB) / 2.0
            x_opt2 = max(0, min(dBA, x_opt2))
            for x in [int(x_opt2), int(x_opt2)+1]:
                x = max(0, min(dBA, x))
                t = max(dB + x, dA + (dBA - x))
                best = min(best, t)
            
            out.append(best)
    
    print('\n'.join(map(str, out)))

solve()