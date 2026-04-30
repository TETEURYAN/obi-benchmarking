import sys
from collections import deque
input = sys.stdin.readline

def main():
    import sys
    from sys import setrecursionlimit
    
    data = sys.stdin.read().split()
    idx = 0
    
    N = int(data[idx]); idx += 1
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1
    
    # Find the cycle
    # Use Floyd or coloring
    color = [0] * (N + 1)  # 0=unvisited, 1=in progress, 2=done
    on_cycle = [False] * (N + 1)
    
    # Find cycle nodes
    visited = [0] * (N + 1)
    in_cycle = [False] * (N + 1)
    
    # Since there's exactly one cycle, we can find it
    # by following paths
    node_state = [0] * (N + 1)  # 0=unvisited, 1=visiting, 2=visited
    
    cycle_nodes = set()
    
    # Find cycle: follow from any unvisited node
    for start in range(1, N + 1):
        if node_state[start] == 0:
            path = []
            node = start
            while node_state[node] == 0:
                node_state[node] = 1
                path.append(node)
                node = F[node]
            if node_state[node] == 1:
                # Found cycle
                cycle_start = node
                in_cycle_flag = False
                for n in path:
                    if n == cycle_start:
                        in_cycle_flag = True
                    if in_cycle_flag:
                        in_cycle[n] = True
                        cycle_nodes.add(n)
            for n in path:
                node_state[n] = 2
    
    # For each node, compute:
    # dist_to_cycle[v] = distance from v to the cycle entry point
    # cycle_entry[v] = which cycle node v enters
    
    dist_to_cycle = [0] * (N + 1)
    cycle_entry = [0] * (N + 1)
    
    for v in range(1, N + 1):
        if in_cycle[v]:
            dist_to_cycle[v] = 0
            cycle_entry[v] = v
    
    # For non-cycle nodes, follow until cycle
    # Use memoization
    memo_dist = [-1] * (N + 1)
    memo_entry = [-1] * (N + 1)
    
    for v in range(1, N + 1):
        if in_cycle[v]:
            memo_dist[v] = 0
            memo_entry[v] = v
    
    def get_dist_entry(v):
        if memo_dist[v] != -1:
            return memo_dist[v], memo_entry[v]
        path = []
        node = v
        while memo_dist[node] == -1:
            path.append(node)
            node = F[node]
        d, e = memo_dist[node], memo_entry[node]
        for i, n in enumerate(reversed(path)):
            memo_dist[n] = d + i + 1
            memo_entry[n] = e
        return memo_dist[v], memo_entry[v]
    
    for v in range(1, N + 1):
        get_dist_entry(v)
    
    # Build cycle order for distance computation on cycle
    # Find cycle length and position of each cycle node
    cycle_list = []
    # Start from any cycle node
    start_cycle = next(iter(cycle_nodes))
    node = start_cycle
    while True:
        cycle_list.append(node)
        node = F[node]
        if node == start_cycle:
            break
    
    cycle_len = len(cycle_list)
    cycle_pos = {}
    for i, v in enumerate(cycle_list):
        cycle_pos[v] = i
    
    # Distance on cycle from node a to node b (directed): 
    # (pos[b] - pos[a]) % cycle_len
    # We want minimum meeting time
    
    results = []
    for _ in range(Q):
        A = int(data[idx]); idx += 1
        B = int(data[idx]); idx += 1
        
        if A == B:
            results.append(0)
            continue
        
        dA = memo_dist[A]
        eA = memo_entry[A]
        dB = memo_dist[B]
        eB = memo_entry[B]
        
        # Both need to reach cycle, then meet on cycle
        # If they enter same cycle node
        if eA == eB:
            # They meet at eA at time max(dA, dB)
            # But could they meet before on the path?
            # Check if one is ancestor of other on peripheral path
            # Actually min time is max(dA, dB) if same entry
            # But if A is on path to B or vice versa
            results.append(max(dA, dB))
            continue
        
        # They enter cycle at different points
        # After dA steps A is at eA, after dB steps B is at eB
        # Then they move on cycle simultaneously
        # A moves from eA, B moves from eB
        # After t more steps: A at pos (posA + t) % L, B at pos (posB + t) % L
        # Meet when (posA + t) % L == (posB + t) % L => posA == posB, contradiction
        # So they can only meet if they're at same position
        # Wait - on cycle both move forward. They meet when positions equal.
        # posA + t ≡ posB + t (mod L) => posA ≡ posB always or never
        # So they can only meet at entry points before fully on cycle
        # Actually one can wait... no, movement is mandatory each step? 
        # Re-read: they move simultaneously, each step traverses one road
        # They can STOP at any city (don't have to keep moving)
        
        posA = cycle_pos[eA]
        posB = cycle_pos[eB]
        
        best = float('inf')
        # A arrives at cycle at time dA, B at time dB
        # After that, one can stay, other moves on cycle
        # Try all: A stays at eA, B walks to eA: dist on cycle from eB to eA
        # Time = max(dA, dB + dist(eB->eA))
        # Or B stays at eB, A walks to eB
        # Time = max(dB, dA + dist(eA->eB))
        # Or they meet somewhere on cycle
        
        for tA_extra in range(cycle_len):
            # A moves tA_extra steps on cycle after arriving
            meet_pos = (posA + tA_extra) % cycle_len
            # B needs to reach meet_pos: dB + steps from eB to meet_pos
            steps_B = (meet_pos - posB) % cycle_len
            time = max(dA + tA_extra, dB + steps_B)
            if time < best:
                best = time
        
        results.append(best)
    
    print('\n'.join(map(str, results)))

main()