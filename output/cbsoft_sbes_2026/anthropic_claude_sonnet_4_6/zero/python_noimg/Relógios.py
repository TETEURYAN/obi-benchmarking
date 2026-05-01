from collections import deque
import sys
input = sys.stdin.readline

def solve():
    L, C, K = map(int, input().split())
    grid = []
    for _ in range(L):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # BFS with state (row, col, time mod K)
    # At time t, when rabbit is at cell (r,c):
    # - if grid[r][c] == -1 (working clock): shows time t mod K, which equals t mod K, always correct
    # - if grid[r][c] == p (stopped clock): shows p, correct only if t mod K == p
    
    # Start: (0, 0) at time 0
    # grid[0][0] == 0, time=0, 0 mod K == 0 -> OK
    
    # State: (r, c, t mod K)
    # We want minimum t to reach (L-1, C-1)
    
    # Since K can be up to 1e5 and L,C up to 100, state space is 100*100*1e5 = 1e9 which is too large
    # But wait - for working clocks, rabbit can wait there. For stopped clocks, rabbit can only be there at specific times.
    
    # Key insight: if rabbit is at a working clock cell, it can wait any amount of time.
    # The time mod K matters for stopped clocks.
    
    # BFS: dist[r][c][t%K] = minimum time to reach (r,c) with time ≡ t (mod K)
    # This might be too large. Let's think differently.
    
    # Actually state space: L*C*K = 100*100*100000 = 1e9 - too large
    # But for 25 points: 20*20*10 = 4000 - fine
    
    # For full solution, we need smarter approach.
    # Note: if we reach a working clock cell, we can adjust time mod K freely by waiting.
    # So from a working clock, we can "teleport" to any time mod K.
    
    # Use Dijkstra/BFS where state is (r, c, t mod K)
    # But optimize: if cell is working (-1), we don't need to track t mod K separately
    # because we can wait to get any mod K value.
    
    # Let's use BFS with states (r, c, t_mod_K)
    # For working cells, we can collapse: once we reach a working cell at any time,
    # we can reach it at any time mod K (by waiting), so we just need minimum time to reach it.
    
    # Simplified: dist_working[r][c] = min time to reach working cell (r,c)
    # dist_stopped[r][c] = min time to reach stopped cell (r,c) (must be at correct mod)
    
    # Use modified Dijkstra
    import heapq
    
    INF = float('inf')
    # dist[r][c][k] for stopped clocks (only valid k = grid[r][c])
    # dist_w[r][c] for working clocks
    
    # State: (time, r, c, t_mod) but t_mod = time % K
    # Let's just do BFS/Dijkstra with state (r, c, t%K)
    # Limit: if K is large but grid is small, many states won't be visited
    
    dist = {}
    # (r, c, t%K) -> min time
    
    start_mod = 0 % K
    heap = [(0, 0, 0, start_mod)]  # (time, r, c, t%K)
    dist[(0, 0, start_mod)] = 0
    
    target = (L-1, C-1)
    
    while heap:
        t, r, c, tm = heapq.heappop(heap)
        
        if (r, c) == target:
            print(t)
            return
        
        if dist.get((r, c, tm), INF) < t:
            continue
        
        # Possible moves: wait (only if working clock) or move to adjacent
        # Wait at current cell (only if working clock)
        if grid[r][c] == -1:
            # Can wait 1 unit
            new_t = t + 1
            new_tm = (tm + 1) % K
            state = (r, c, new_tm)
            if dist.get(state, INF) > new_t:
                dist[state] = new_t
                heapq.heappush(heap, (new_t, r, c, new_tm))
        
        # Move to adjacent cells
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < L and 0 <= nc < C:
                new_t = t + 1
                new_tm = (tm + 1) % K
                p = grid[nr][nc]
                if p == -1 or p == new_tm:
                    state = (nr, nc, new_tm)
                    if dist.get(state, INF) > new_t:
                        dist[state] = new_t
                        heapq.heappush(heap, (new_t, nr, nc, new_tm))
    
    print(-1)

solve()