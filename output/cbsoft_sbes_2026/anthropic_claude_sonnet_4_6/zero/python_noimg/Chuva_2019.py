from collections import deque

def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    grid = []
    for i in range(N):
        grid.append(list(input_data[idx])); idx += 1
    
    # BFS/simulation using the rules
    # c(i,j) becomes 'o' if it's '.' and:
    # 1. c(i-1,j) = 'o'
    # 2. c(i,j-1) = 'o' and c(i+1,j-1) = '#'
    # 3. c(i,j+1) = 'o' and c(i+1,j+1) = '#'
    
    # We need to propagate iteratively
    # Use a queue of newly set 'o' positions and check neighbors
    
    queue = deque()
    
    # Find initial 'o'
    for j in range(M):
        if grid[0][j] == 'o':
            queue.append((0, j))
            break
    
    def try_set(i, j, queue, grid, N, M):
        if 0 <= i < N and 0 <= j < M and grid[i][j] == '.':
            grid[i][j] = 'o'
            queue.append((i, j))
    
    while queue:
        i, j = queue.popleft()
        # Current cell (i,j) is 'o', check what it can wet
        
        # Rule 1: cell below (i+1, j) becomes 'o' if it's '.'
        if i + 1 < N and grid[i+1][j] == '.':
            try_set(i+1, j, queue, grid, N, M)
        
        # Rule 2: cell (i, j+1) becomes 'o' if c(i+1, j+1) = '#'
        # i.e., current is c(i, j-1)='o', so we wet c(i, j) where j = (j+1)
        # Actually rule 2 says: c(i,j) becomes 'o' if c(i,j-1)='o' and c(i+1,j-1)='#'
        # So when (i, j) becomes 'o', check if c(i+1, j) = '#'
        # If yes, then c(i, j+1) can become 'o' (if it's '.')
        if i + 1 < N and grid[i+1][j] == '#':
            # c(i, j) = 'o' and c(i+1, j) = '#'
            # So c(i, j+1) satisfies rule 2: c(i, j+1-1)='o' and c(i+1, j+1-1)='#'
            if j + 1 < M and grid[i][j+1] == '.':
                try_set(i, j+1, queue, grid, N, M)
        
        # Rule 3: c(i,j) becomes 'o' if c(i,j+1)='o' and c(i+1,j+1)='#'
        # So when (i,j) becomes 'o', check if c(i+1,j)='#'
        # If yes, then c(i, j-1) can become 'o'
        if i + 1 < N and grid[i+1][j] == '#':
            if j - 1 >= 0 and grid[i][j-1] == '.':
                try_set(i, j-1, queue, grid, N, M)
        
        # Also need to check: when (i,j) becomes 'o', 
        # can it trigger rule 2 for (i, j+1)?
        # Rule 2 for cell (r,c): c(r,c-1)='o' and c(r+1,c-1)='#'
        # Here r=i, c=j+1: c(i,j)='o' and c(i+1,j)='#' -> already handled above
        
        # Rule 3 for cell (r,c): c(r,c+1)='o' and c(r+1,c+1)='#'
        # Here r=i, c=j-1: c(i,j)='o' and c(i+1,j)='#' -> already handled above
        
        # Also: when (i,j) becomes 'o', check neighbors that might now satisfy rules
        # Rule 2: cell (i, j) could be wetted by (i, j-1)='o' if c(i+1,j-1)='#'
        # But we need to check if setting (i,j)='o' enables (i, j+1) via rule 2
        # That's: c(i, j+1-1)=c(i,j)='o' and c(i+1, j+1-1)=c(i+1,j)='#' -> handled
        
        # Rule 3: c(i, j-1) via rule 3: c(i, j-1+1)=c(i,j)='o' and c(i+1,j-1+1)=c(i+1,j)='#' -> handled
    
    for row in grid:
        print(''.join(row))

solve()