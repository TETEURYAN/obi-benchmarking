from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    L = int(input_data[idx]); idx+=1
    C = int(input_data[idx]); idx+=1
    K = int(input_data[idx]); idx+=1
    
    grid = []
    for i in range(L):
        row = []
        for j in range(C):
            row.append(int(input_data[idx])); idx+=1
        grid.append(row)
    
    # BFS with state (row, col, time mod K)
    # At time t, rabbit is at (r,c)
    # Clock at (r,c):
    #   if P == -1 (working): shows t mod K, always correct
    #   if P >= 0 (stopped): shows P, correct only if t mod K == P
    
    # Start: (0,0) at time 0
    # grid[0][0] == 0, so at time 0, 0 mod K == 0, OK
    
    # State: (r, c, t mod K)
    # We want minimum t to reach (L-1, C-1)
    
    # Since K can be up to 1e5 and grid up to 100x100,
    # total states = 100 * 100 * 1e5 = 1e9, too large
    
    # Key insight: for a working clock, rabbit can always enter (time matches)
    # For a stopped clock with value P, rabbit can only enter when t mod K == P
    # 
    # We can use Dijkstra or BFS with the observation:
    # When rabbit is at a working clock room, they can wait any amount of time
    # When rabbit is at a stopped clock room with value P, they must leave at time t where t mod K == P
    # Actually they can only BE there when t mod K == P
    
    # Let's think differently:
    # State = (r, c, t mod K)
    # Transitions:
    # 1. Move to adjacent cell (r2,c2) at time t+1: valid if clock at (r2,c2) shows correct time at t+1
    # 2. Wait in current cell (only if working clock, P==-1): stay at (r,c) at time t+1
    #    (stopped clock: can't wait because next moment t+1 mod K != P unless K==1)
    
    # BFS since all edges have weight 1 (each action takes 1 time unit)
    # State space: L * C * K
    # With L,C<=100, K<=1e5: 10^9 states - too large
    
    # But we can use BFS with actual time, and note that if we visit (r,c) at time t mod K again,
    # we've been in a cycle and won't improve.
    
    # visited[r][c][t mod K] = True if visited
    
    INF = float('inf')
    # visited array
    visited = [[[False]*K for _ in range(C)] for _ in range(L)]
    
    # Check start
    # grid[0][0] should be 0 (stopped at 0), time=0, 0 mod K = 0 == 0, OK
    
    queue = deque()
    queue.append((0, 0, 0))  # (row, col, time)
    visited[0][0][0] = True
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while queue:
        r, c, t = queue.popleft()
        
        if r == L-1 and c == C-1:
            print(t)
            return
        
        nt = t + 1
        nt_mod = nt % K
        
        # Option 1: Move to adjacent cells
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < L and 0 <= nc < C:
                p = grid[nr][nc]
                # Check if clock at (nr,nc) shows correct time at nt
                if p == -1 or p == nt_mod:
                    if not visited[nr][nc][nt_mod]:
                        visited[nr][nc][nt_mod] = True
                        queue.append((nr, nc, nt))
        
        # Option 2: Wait in current cell (only if working clock)
        if grid[r][c] == -1:
            if not visited[r][c][nt_mod]:
                visited[r][c][nt_mod] = True
                queue.append((r, c, nt))
    
    print(-1)

solve()