import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx]); idx+=1
    C = int(data[idx]); idx+=1
    K = int(data[idx]); idx+=1
    
    grid = []
    for i in range(L):
        row = []
        for j in range(C):
            row.append(int(data[idx])); idx+=1
        grid.append(row)
    
    # State: (time, row, col)
    # At time t, at cell (r,c):
    # - if grid[r][c] == -1 (working clock): shows time t % K, always correct
    # - if grid[r][c] == p (stopped clock): shows p, correct only if t % K == p
    
    # We can wait in a cell only if clock is working (always correct)
    # We cannot enter or wait in a cell where clock shows wrong time
    
    # Start: (0, 0, 0), grid[0][0] = 0, time=0, 0%K=0 -> correct
    # End: (L-1, C-1)
    
    # Dijkstra on (time, r, c)
    # But time can be large... 
    # Max time: we might need to wait. If a cell has stopped clock p, 
    # we can only be there at time t where t%K == p.
    # Working clocks: always fine, can wait any amount.
    
    # The key insight: if we're at a working clock cell at time t,
    # we can wait up to K-1 steps to sync with a neighbor's stopped clock.
    # So time can grow but is bounded by... 
    # In worst case, path length is L+C-2 moves, plus waiting.
    # Maximum wait at any cell: K-1 steps. Number of cells: L*C <= 10000.
    # So max time ~ (L+C) * K ~ 200 * 10^5 = 2*10^7. That's manageable with Dijkstra.
    
    # dist[r][c] = minimum time to reach (r,c) with valid clock
    # But we need dist as minimum time, and since we can only be at (r,c) at specific times
    # (for stopped clocks: only t%K == p), we track minimum time.
    
    # For stopped clock cells: we can only arrive at time t where t%K == p.
    # For working clock cells: we can arrive at any time, and wait.
    
    # Dijkstra: state is (time, r, c)
    # dist[r][c] = min time to be validly at (r,c)
    
    INF = float('inf')
    dist = [[INF]*C for _ in range(L)]
    dist[0][0] = 0
    
    pq = [(0, 0, 0)]
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while pq:
        t, r, c = heapq.heappop(pq)
        
        if t > dist[r][c]:
            continue
        
        if r == L-1 and c == C-1:
            print(t)
            return
        
        # From (r,c) at time t, we can move to neighbors
        # If current cell is working (-1), we can also wait here
        
        # Generate possible departure times from (r,c)
        # If grid[r][c] == -1 (working): we can depart at t, t+1, t+2, ... t+K-1
        #   (waiting more than K-1 is pointless since it cycles)
        # If grid[r][c] == p (stopped): we can only be here at time t (already validated)
        #   so we depart at time t only (can't wait since waiting means next moment t+1,
        #   and stopped clock at p won't match t+1%K unless p==(t+1)%K)
        #   Actually: can we wait in a stopped clock cell? 
        #   "He can wait in a room whose clock is working"
        #   "He cannot enter, nor wait, in a room whose clock shows wrong time"
        #   So for stopped clock: at time t+1, clock shows p but time is t+1, 
        #   valid only if (t+1)%K == p. So we can only stay if each moment is valid.
        #   Effectively for stopped clock p: can only be there at times where time%K==p.
        #   So we can wait K steps at a time (stay K units). But that's same as not waiting.
        #   So from stopped clock: depart at t only (or t+K, t+2K... but those give same mod).
        
        p_cur = grid[r][c]
        
        if p_cur == -1:
            # Can wait 0..K-1 steps
            departure_times = range(t, t + K)
        else:
            # Can only depart at t (stopped clock, already at correct time)
            departure_times = [t]
        
        for dt in departure_times:
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < L and 0 <= nc < C:
                    arrive_time = dt + 1
                    p_next = grid[nr][nc]
                    # Check if valid to be at (nr,nc) at arrive_time
                    if p_next == -1 or arrive_time % K == p_next:
                        if arrive_time < dist[nr][nc]:
                            dist[nr][nc] = arrive_time
                            heapq.heappush(pq, (arrive_time, nr, nc))
    
    print(-1)

solve()