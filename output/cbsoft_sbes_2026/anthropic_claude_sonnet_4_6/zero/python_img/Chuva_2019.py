from collections import deque

def solve():
    import sys
    input_data = sys.stdin.buffer.read().decode()
    tokens = input_data.split()
    idx = 0
    N = int(tokens[idx]); idx += 1
    M = int(tokens[idx]); idx += 1
    
    grid = []
    for i in range(N):
        grid.append(list(tokens[idx])); idx += 1
    
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
        # Current cell is 'o', propagate to neighbors based on rules
        
        # Rule 1: cell below (i+1, j) becomes 'o' if grid[i+1][j] == '.'
        # i.e., c(i+1,j) becomes 'o' because c(i+1-1, j) = c(i,j) = 'o'
        ni, nj = i+1, j
        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == '.':
            grid[ni][nj] = 'o'
            queue.append((ni, nj))
        
        # Rule 2: c(i, j+1) becomes 'o' if c(i, j+1-1) = c(i,j) = 'o' and c(i+1, j+1-1) = c(i+1, j) = '#'
        # So cell (i, j+1) can be set if current is 'o' and grid[i+1][j] == '#'
        ni, nj = i, j+1
        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == '.':
            # check c(i+1, j) == '#'
            if i+1 < N and grid[i+1][j] == '#':
                grid[ni][nj] = 'o'
                queue.append((ni, nj))
        
        # Rule 3: c(i, j-1) becomes 'o' if c(i, j-1+1) = c(i,j) = 'o' and c(i+1, j-1+1) = c(i+1, j) = '#'
        # So cell (i, j-1) can be set if current is 'o' and grid[i+1][j] == '#'
        ni, nj = i, j-1
        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == '.':
            # check c(i+1, j) == '#'
            if i+1 < N and grid[i+1][j] == '#':
                grid[ni][nj] = 'o'
                queue.append((ni, nj))
    
    out = []
    for row in grid:
        out.append(''.join(row))
    print('\n'.join(out))

solve()