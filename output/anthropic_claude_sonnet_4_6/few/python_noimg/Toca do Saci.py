import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    grid = []
    start = None
    
    for i in range(N):
        row = []
        for j in range(M):
            val = int(data[idx]); idx += 1
            row.append(val)
            if val == 2:
                start = (i, j)
        grid.append(row)
    
    # BFS/path following: from start (2), follow cells with value 1, 2, or 3
    # No ambiguity: at each step only one marked neighbor to go to
    # Count rooms passed including start and exit
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    cur = start
    prev = None
    count = 1  # count current room
    
    while True:
        r, c = cur
        if grid[r][c] == 3:
            break
        
        next_cell = None
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if (nr, nc) != prev and grid[nr][nc] in (1, 2, 3):
                    next_cell = (nr, nc)
                    break
        
        if next_cell is None:
            break
        
        prev = cur
        cur = next_cell
        count += 1
    
    print(count)

main()