import sys
from sys import stdin

def solve():
    input = stdin.read().split()
    idx = 0
    N = int(input[idx]); idx += 1
    grid = []
    for i in range(N):
        grid.append(input[idx]); idx += 1
    
    # Direction mappings
    # 'V' -> down (row+1, col)
    # 'A' -> up (row-1, col)
    # '<' -> left (row, col-1)
    # '>' -> right (row, col+1)
    
    dir_map = {
        'V': (1, 0),
        'A': (-1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    
    # State for each cell: 0 = unvisited, 1 = safe, 2 = unsafe, 3 = in current path
    state = [[0] * N for _ in range(N)]
    
    def dfs_iterative(start_r, start_c):
        # We'll trace the path from start
        # If we hit a cell already known safe/unsafe, we can determine the result
        # If we hit a cell in current path, it's a cycle -> safe
        # If we go out of bounds -> unsafe
        
        path = []
        path_set = {}
        
        r, c = start_r, start_c
        
        while True:
            if r < 0 or r >= N or c < 0 or c >= N:
                # unsafe - mark all in path as unsafe
                for pr, pc in path:
                    state[pr][pc] = 2
                return
            
            if state[r][c] == 1:
                # safe - mark all in path as safe
                for pr, pc in path:
                    state[pr][pc] = 1
                return
            
            if state[r][c] == 2:
                # unsafe - mark all in path as unsafe
                for pr, pc in path:
                    state[pr][pc] = 2
                return
            
            if (r, c) in path_set:
                # cycle detected - everything from the cycle point onwards is safe
                # and everything in path before is also safe (leads to cycle)
                for pr, pc in path:
                    state[pr][pc] = 1
                return
            
            # Mark as in current path
            path_set[(r, c)] = len(path)
            path.append((r, c))
            
            dr, dc = dir_map[grid[r][c]]
            r, c = r + dr, c + dc
    
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0:
                dfs_iterative(i, j)
    
    count = sum(1 for i in range(N) for j in range(N) if state[i][j] == 1)
    print(count)

solve()