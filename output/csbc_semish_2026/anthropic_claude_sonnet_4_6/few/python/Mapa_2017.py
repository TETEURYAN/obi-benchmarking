import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    
    grid = []
    for i in range(L):
        grid.append(data[idx]); idx += 1
    
    # Find starting position 'o'
    start_r, start_c = -1, -1
    for i in range(L):
        for j in range(C):
            if grid[i][j] == 'o':
                start_r, start_c = i, j
    
    # From 'o', find the single 'H' neighbor
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # Find first H neighbor of 'o'
    first_r, first_c = -1, -1
    for dr, dc in dirs:
        nr, nc = start_r + dr, start_c + dc
        if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 'H':
            first_r, first_c = nr, nc
            break
    
    # Now traverse the path: prev is start, current is first H
    prev_r, prev_c = start_r, start_c
    cur_r, cur_c = first_r, first_c
    
    while True:
        # Find neighbors of current that are 'H' and not prev
        h_neighbors = []
        for dr, dc in dirs:
            nr, nc = cur_r + dr, cur_c + dc
            if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 'H':
                if (nr, nc) != (prev_r, prev_c):
                    h_neighbors.append((nr, nc))
        
        # Also check 'o' neighbors (but we came from 'o' so it won't be next)
        # Count all H neighbors including prev to determine if endpoint
        all_h_neighbors = []
        for dr, dc in dirs:
            nr, nc = cur_r + dr, cur_c + dc
            if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 'H':
                all_h_neighbors.append((nr, nc))
        
        # Check neighbors including 'o'
        all_neighbors_ho = []
        for dr, dc in dirs:
            nr, nc = cur_r + dr, cur_c + dc
            if 0 <= nr < L and 0 <= nc < C and (grid[nr][nc] == 'H' or grid[nr][nc] == 'o'):
                all_neighbors_ho.append((nr, nc))
        
        # The path constraint: endpoint has exactly 1 H neighbor (from constraints)
        # intermediate has exactly 2 H neighbors
        # We need to check: from current position, how many H neighbors exist
        # If only 1 H neighbor total (which is prev), then current is endpoint
        
        if len(all_h_neighbors) == 1 and all_h_neighbors[0] == (prev_r, prev_c):
            # current is the endpoint
            print(cur_r + 1, cur_c + 1)
            return
        
        if len(h_neighbors) == 0:
            # No next H neighbor, current is endpoint
            print(cur_r + 1, cur_c + 1)
            return
        
        # Move to next
        next_r, next_c = h_neighbors[0]
        prev_r, prev_c = cur_r, cur_c
        cur_r, cur_c = next_r, next_c

solve()