import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = int(input_data[idx]); idx += 1
    Q = int(input_data[idx]); idx += 1
    queries = []
    for _ in range(Q):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        queries.append((a, b))
    
    # Find cycle nodes
    visited = [0] * (N + 1)  # 0=unvisited, 1=in progress, 2=done
    on_cycle = [False] * (N + 1)
    
    # Find the cycle using tortoise and hare or simple traversal
    # Since each node has exactly one outgoing edge, we can find cycle
    in_cycle = [False] * (N + 1)
    
    # Find cycle: follow any node until we revisit
    state = [0] * (N + 1)  # 0=unvisited, 1=in stack, 2=done
    
    for start in range(1, N + 1):
        if state[start] == 0:
            path = []
            node = start
            while state[node] == 0:
                state[node] = 1
                path.append(node)
                node = F[node]
            if state[node] == 1:
                # Found cycle
                # Find where cycle starts in path
                cycle_start = node
                in_cycle_set = False
                for n in path:
                    if n == cycle_start:
                        in_cycle_set = True
                    if in_cycle_set:
                        in_cycle[n] = True
            for n in path:
                state[n] = 2
    
    # Get cycle nodes in order
    cycle_nodes = [i for i in range(1, N + 1) if in_cycle[i]]
    cycle_len = len(cycle_nodes)
    
    # Build cycle order: start from cycle_nodes[0], follow F
    # Find cycle order
    cycle_start = cycle_nodes[0]
    cycle_order = [cycle_start]
    cur = F[cycle_start]
    while cur != cycle_start:
        cycle_order.append(cur)
        cur = F[cur]
    cycle_len = len(cycle_order)
    
    # Map cycle node -> position in cycle
    cycle_pos = {}
    for i, node in enumerate(cycle_order):
        cycle_pos[node] = i
    
    # For each node, compute:
    # dist_to_cycle[node] = distance from node to the cycle
    # entry_node[node] = which cycle node it enters
    dist_to_cycle = [0] * (N + 1)
    entry_node = [0] * (N + 1)
    
    for node in range(1, N + 1):
        if in_cycle[node]:
            dist_to_cycle[node] = 0
            entry_node[node] = node
    
    # For non-cycle nodes, follow path to cycle
    # Use memoization
    memo_dist = [-1] * (N + 1)
    memo_entry = [-1] * (N + 1)
    
    for node in range(1, N + 1):
        if in_cycle[node]:
            memo_dist[node] = 0
            memo_entry[node] = node
    
    def get_dist_entry(node):
        if memo_dist[node] != -1:
            return memo_dist[node], memo_entry[node]
        path = []
        cur = node
        while memo_dist[cur] == -1:
            path.append(cur)
            cur = F[cur]
        d = memo_dist[cur]
        e = memo_entry[cur]
        for p in reversed(path):
            d += 1
            # Actually need to compute properly
        # Redo
        d = memo_dist[cur]
        e = memo_entry[cur]
        for p in reversed(path):
            memo_entry[p] = e
            memo_dist[p] = d + 1
            d += 1
        # Fix: d was incremented too many times
        # Let's redo
        return memo_dist[node], memo_entry[node]
    
    # Better iterative approach
    for node in range(1, N + 1):
        if memo_dist[node] == -1:
            path = []
            cur = node
            while memo_dist[cur] == -1:
                path.append(cur)
                cur = F[cur]
            base_d = memo_dist[cur]
            base_e = memo_entry[cur]
            for i, p in enumerate(reversed(path)):
                memo_dist[p] = base_d + i + 1
                memo_entry[p] = base_e
    
    out = []
    for a, b in queries:
        if a == b:
            out.append(0)
            continue
        da = memo_dist[a]
        db = memo_dist[b]
        ea = memo_entry[a]
        eb = memo_entry[b]
        
        if ea == eb:
            # Same entry point to cycle
            # They can meet somewhere on the path or at entry
            # Best meeting point: if one is ancestor of other on path
            # da steps from a to cycle, db steps from b to cycle
            # They meet at min(da,db) steps from the one closer
            # Actually: person a takes da steps to reach ea, person b takes db steps
            # If they share path: the one further away walks, other waits or walks back (can't)
            # Meeting point is at distance min(da,db) from cycle entry
            # Time = max(da, db) - but they can meet earlier if on same path
            # Since it's a directed path (tail), a is at depth da, b at depth db from cycle
            # They can only move forward (toward cycle)
            # If da >= db: a needs da steps to reach ea, b needs db steps
            # They can meet at b's position if da - db steps... no, b moves too
            # Let's think: at time t, a is at position da-t from cycle (if da-t>=0) else on cycle
            # b is at position db-t from cycle
            # They meet when at same node
            # On the tail path, node at distance k from cycle is unique (since in-degree <=1 for non-cycle)
            # So they meet when da-t == db-t => da==db, or both on cycle
            # If da != db: they meet on cycle when both reach it
            # Time = max(da, db) but then they're both on cycle at ea
            # Wait if da==db they meet at time da at ea... but maybe earlier on path
            # If same entry and same path: node at dist k from ea is same for both only if da==db
            # Actually if ea==eb, the paths might diverge before ea
            # Hmm, need to check if a is ancestor of b or vice versa
            
            # Check if b is on path from a to cycle
            # Path from a: a -> F[a] -> ... -> ea
            # Path from b: b -> F[b] -> ... -> eb = ea
            # If da > db: a is further, path from a passes through b? Not necessarily
            # We need to check if F^(da-db)[a] == b... 
            # This could be O(N) per query. Need better approach.
            
            # Alternative: for same entry, meeting time is ceil((da+db)/2)? No...
            # 
            # Actually since both move simultaneously toward cycle:
            # At time t: a is at node reached after t steps from a, b similarly
            # They meet if same node at same time t
            # On the linear path to cycle: if a and b are on same path with da > db,
            # then after (da-db) steps, a reaches b's starting position, but b has moved db steps further
            # They never meet on the path unless da==db
            # On cycle: a arrives at ea at time da, b arrives at eb=ea at time db
            # After that both traverse cycle. They meet on cycle.
            # Time to meet on cycle after both are on cycle:
            # a enters cycle at pos cycle_pos[ea] at time da
            # b enters cycle at pos cycle_pos[eb]=cycle_pos[ea] at time db
            # WLOG da <= db. At time db, a is at pos (cycle_pos[ea] + db - da) % cycle_len
            # b is at pos cycle_pos[ea]
            # They need to meet: positions equal mod cycle_len
            # (cycle_pos[ea] + db - da + t) % cycle_len == (cycle_pos[ea] + t) % cycle_len
            # => (db - da) % cycle_len == 0
            # If da == db: meet at time da = db at ea. 
            # If (db-da) % cycle_len == 0: meet at time db at ea
            # Otherwise they never meet on cycle at same time? That can't be right...
            # Wait they DO meet: at time db + t, a is at (cycle_pos[ea] + db-da+t)%cycle_len
            # b is at (cycle_pos[ea] + t) % cycle_len
            # Equal when (db-da) % cycle_len == 0, i.e., t can be anything
            # If db-da not divisible by cycle_len, they never meet??
            # That seems wrong. Oh wait - the meeting point doesn't have to be where both arrive simultaneously following their paths. They can STOP and wait? No - re-read problem.
            # "cada estrada é percorrida em uma unidade de tempo" - they traverse roads
            # Can they stay in a city? The problem says "menor tempo em que elas podem se encontrar"
            # I think they can choose to stay (wait) at a city.
            # If they can wait, then: person with smaller dist waits at cycle entry, other arrives later.
            # Time = max(da, db). But maybe they can meet earlier on the path.
            # If da > db and b is on path from a to cycle: a reaches b's pos at time (da-db), b has moved to pos (da-db) steps ahead. They don't meet unless da==db.
            # Hmm but if b can wait: b waits at its start, a walks da-db steps to reach... not b's pos unless on same path.
            
            # I'll assume they can wait (stay at a node).
            # Then optimal: 
            # If on same linear path (one is ancestor of other toward cycle):
            #   The one further back walks, the closer one waits. Time = (da - db) if a is further and b is between a and cycle... but b might not be on a's path.
            # This requires knowing if they share path.
            
            # Let me reconsider the structure:
            # Each non-cycle node has exactly one outgoing edge and at most one incoming edge (from problem constraints: "a cada cidade que não pertence ao ciclo chega no máximo uma estrada")
            # So the peripheral paths are simple chains (trees that are paths) leading to cycle nodes.
            # 
            # For two nodes a, b with same entry ea=eb:
            # They are on the same chain. 
            # da = distance from a to ea, db = distance from b to ea.
            # WLOG da >= db.
            # Is b on the path from a to ea? 
            # The path from a to ea has exactly da+1 nodes at distances da, da-1, ..., 1, 0 from ea.
            # b is at distance db from ea on the same chain.
            # Since it's a simple path (chain), yes b IS on the path from a to ea (since da >= db).
            # So a can reach b in (da - db) steps. If b waits, they meet in (da - db) steps.
            # But b could also move toward ea and they meet somewhere in between.
            # If a moves and b moves: at time t, a is at distance da-t from ea, b is at distance db-t from ea (if db-t >= 0).
            # They meet when da-t == db-t => impossible unless da==db.
            # OR b waits: a reaches b in da-db steps. Time = da-db.
            # OR a waits: b moves away from a toward ea, a then chases... a can reach b's original pos in da-db steps but b is gone.
            # Best: b waits, a walks to b. Time = da - db.
            # But wait, can they meet even earlier? What if they meet at some intermediate node?
            # a starts at distance da, b at distance db (da >= db). 
            # If b waits at its position (distance db from ea):
            #   a reaches b in da-db steps. Time = da-db.
            # If b moves 1 step (to distance db-1):
            #   a needs da-(db-1) = da-db+1 steps to reach that position. But b moved there in 1 step.
            #   They meet if a arrives at db-1 at same time b is there: a arrives at time da-db+1, b arrives at time 1. Not same unless da-db+1==1 => da==db. 
            # So optimal is b waits, time = da - db. 
            # Actually even simpler: they can meet at b's position with b waiting. Time = da-db.
            # Can they do better? Meet at a's position: b needs to go backward, impossible (directed).
            # Meet between a and b: a walks k steps (0<=k<=da-db), b waits. a is at da-k, b is at db. Meet when da-k==db => k=da-db. Same answer.
            # So for same entry, same chain: time = da - db (= |da-db|).
            
            ans = abs(da - db)
        else:
            # Different entry points
            # Both walk to their cycle entries, then traverse cycle
            # They can also meet on cycle
            # Time to reach cycle: da for a, db for b
            # On cycle, a enters at position pa = cycle_pos[ea] at time da
            # b enters at position pb = cycle_pos[eb] at time db
            # After entering cycle, they move along cycle (can also wait)
            # 
            # We want minimum time T such that there exists a meeting point on cycle
            # At time T:
            # a has been on cycle for (T - da) steps (if T >= da), position = (pa + T - da) % cycle_len
            # b has been on cycle for (T - db) steps (if T >= db), position = (pb + T - db) % cycle_len
            # They can wait, so a can be at any position (pa + k) % cycle_len for 0 <= k <= T-da
            # Similarly b at (pb + j) % cycle_len for 0 <= j <= T-db
            # They meet if (pa + k) % cycle_len == (pb + j) % cycle_len for some valid k, j
            # i.e., (pa - pb + k - j) % cycle_len == 0
            # i.e., k - j ≡ pb - pa (mod cycle_len)
            # 
            # We need T >= max(da, db) (both must reach cycle first... actually one might wait for other)
            # Actually minimum T is when both are on cycle and can be at same position.
            # 
            # Let T = max(da, db). Then:
            # a can be at positions pa, pa+1, ..., pa+(T-da) mod cycle_len (any of these)
            # b can be at positions pb, pb+1, ..., pb+(T-db) mod cycle_len
            # 
            # The ranges of positions reachable:
            # a: pa to pa+(T-da) (mod cycle_len), that's (T-da+1) consecutive positions
            # b: pb to pb+(T-db) (mod cycle_len), that's (T-db+1) consecutive positions
            # 
            # If T-da + T-db + 2 >= cycle_len (i.e., total coverage >= cycle_len), they definitely meet.
            # Otherwise need to check overlap.
            #
            # This is getting complex. Let me think differently.
            #
            # Minimum time T:
            # T >= da (a must reach cycle)
            # T >= db (b must reach cycle)  
            # After T steps, a can be at (pa + s) % cycle_len for 0 <= s <= T-da
            # After T steps, b can be at (pb + t) % cycle_len for 0 <= t <= T-db
            # Need (pa + s) % L == (pb + t) % L
            # => s - t ≡ pb - pa (mod L)
            # => s ≡ pb - pa + t (mod L)
            # For given T, we need s in [0, T-da] and t in [0, T-db] with s-t ≡ pb-pa (mod L)
            # 
            # Let diff = (pb - pa) % L
            # We need s - t = diff + k*L for some integer k
            # s = t + diff + k*L
            # s in [0, T-da], t in [0, T-db]
            # t + diff + k*L in [0, T-da]
            # t in [0, T-db]
            # 
            # For k=0: s = t + diff, need t+diff <= T-da and t >= 0 and t <= T-db
            #   t in [0, min(T-db, T-da-diff)] if diff >= 0
            #   Valid if T-da-diff >= 0 and T-db >= 0, i.e., T >= da+diff and T >= db
            #   Since diff = (pb-pa)%L >= 0, T >= da + diff and T >= db
            #   T >= max(da + diff, db) where diff = (pb-pa)%L
            # For k=-1: s = t + diff - L, need s >= 0 => t >= L-diff, and s <= T-da => t <= T-da-diff+L
            #   t in [L-diff, min(T-db, T-da+L-diff)]
            #   Valid if L-diff <= T-db and T-da+L-diff >= L-diff => T >= da
            #   T >= db + L - diff and T >= da
            #   T >= max(db + L - diff, da) where L-diff = (pa-pb)%L
            # 
            # So minimum T is min of:
            #   max(da + diff, db) where diff = (pb-pa)%L
            #   max(db + (L-diff), da) where L-diff = (pa-pb)%L
            # 
            # (and T must be >= max(da,db) which is already covered)
            
            L = cycle_len
            pa = cycle_pos[ea]
            pb = cycle_pos[eb]
            diff1 = (pb - pa) % L  # clockwise distance from ea to eb
            diff2 = (pa - pb) % L  # clockwise distance from eb to ea = L - diff1
            
            # Option 1: a waits at pa+diff1... no let me use formula
            # T1 = max(da + diff1, db)  [a moves diff1 steps on cycle to meet b at pb, b waits]
            # T2 = max(db + diff2, da)  [b moves diff2 steps on cycle to meet a at pa, a waits]
            # But they can also both move, which might give better results
            # Actually the formula above covers all cases (k=0 and k=-1 cover the two directions)
            # For k other values, T would be larger.
            
            T1 = max(da + diff1, db)
            T2 = max(db + diff2, da)
            ans = min(T1, T2)
        
        out.append(ans)
    
    sys.stdout.write('\n'.join(map(str, out)) + '\n')

solve()