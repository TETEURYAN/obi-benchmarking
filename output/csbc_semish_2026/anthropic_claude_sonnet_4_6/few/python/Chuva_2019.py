import sys
from collections import deque

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    first_line = data[idx].split()
    idx += 1
    N = int(first_line[0])
    M = int(first_line[1])
    
    grid = []
    for i in range(N):
        if idx < len(data):
            row = data[idx]
            idx += 1
        else:
            row = ''
        # Pad or trim to M characters
        if len(row) < M:
            row = row + '.' * (M - len(row))
        else:
            row = row[:M]
        grid.append(list(row))
    
    # BFS/simulation using the rules
    # We'll use a queue of positions that are 'o' and need to propagate
    # Rules: c(i,j)='.' becomes 'o' if:
    # 1. c(i-1,j)='o'
    # 2. c(i,j-1)='o' and c(i+1,j-1)='#'
    # 3. c(i,j+1)='o' and c(i+1,j+1)='#'
    
    wet = [[False]*M for _ in range(N)]
    queue = deque()
    
    # Find initial 'o' positions
    for j in range(M):
        if grid[0][j] == 'o':
            wet[0][j] = True
            queue.append((0, j))
    
    def try_wet(i, j, q):
        if 0 <= i < N and 0 <= j < M and grid[i][j] == '.' and not wet[i][j]:
            wet[i][j] = True
            grid[i][j] = 'o'
            q.append((i, j))
    
    while queue:
        i, j = queue.popleft()
        # This cell (i,j) is 'o', try to propagate
        
        # Rule 1: cell below (i+1, j) can become 'o' if it's '.'
        if i+1 < N and grid[i+1][j] == '.':
            try_wet(i+1, j, queue)
        
        # Rule 2: cell (i, j+1) can become 'o' if c(i+1,j+1)='#'
        # i.e., current cell is (i,j)='o', check if (i,j+1) should become wet
        # c(i,j+1)='.' becomes 'o' if c(i,j)='o' and c(i+1,j)='#'
        # Wait, let me re-read the rules carefully.
        # c(i,j-1)='o' and c(i+1,j-1)='#' => c(i,j) becomes 'o'
        # So if current is (r,c)='o', then cell (r, c+1) can become 'o' if c(r+1,c)='#'
        if j+1 < M and grid[i][j+1] == '.' and i+1 < N and grid[i+1][j] == '#':
            try_wet(i, j+1, queue)
        
        # Rule 3: c(i,j+1)='o' and c(i+1,j+1)='#' => c(i,j) becomes 'o'
        # So if current is (r,c)='o', then cell (r, c-1) can become 'o' if c(r+1,c)='#'
        if j-1 >= 0 and grid[i][j-1] == '.' and i+1 < N and grid[i+1][j] == '#':
            try_wet(i, j-1, queue)
        
        # Also need to re-check neighbors that might now satisfy conditions
        # When (i,j) becomes 'o', check if (i, j+1) satisfies rule 2 from its perspective
        # (i, j+1) becomes 'o' if c(i, j)='o' and c(i+1, j)='#' -- already handled above
        # But also need: if (i,j) becomes 'o', does it help (i-1, j) via rule? No, rules go down.
        # Check rule 1 for cell above: no, rule 1 says i-1 must be 'o' to wet i.
        # Already handled: when (i,j) becomes 'o', wet (i+1,j) via rule 1.
        
        # Need to also propagate horizontally when on a shelf edge
        # The horizontal propagation continues, so when (i,j+1) becomes 'o' on a shelf,
        # it will in turn wet (i,j+2) etc. That's handled by BFS naturally.
    
    result = []
    for i in range(N):
        result.append(''.join(grid[i]))
    print('\n'.join(result))

solve()