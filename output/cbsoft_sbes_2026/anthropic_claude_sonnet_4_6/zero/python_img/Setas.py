import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    grid = []
    for i in range(1, n + 1):
        grid.append(input_data[i])
    
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
    
    # State for each cell:
    # 0 = unvisited
    # 1 = in current path (being explored)
    # 2 = safe (confirmed)
    # 3 = unsafe (confirmed)
    
    state = [[0] * n for _ in range(n)]
    
    # We'll use iterative DFS to avoid recursion limit issues
    # For each unvisited cell, follow the path until we hit:
    # - Out of bounds -> all cells in path are unsafe
    # - A cell already marked safe -> all cells in path are safe
    # - A cell already marked unsafe -> all cells in path are unsafe
    # - A cell in current path (cycle) -> all cells in cycle are safe, and all leading to cycle are safe
    
    safe_count = 0
    
    for start_r in range(n):
        for start_c in range(n):
            if state[start_r][start_c] != 0:
                continue
            
            # Follow the path from (start_r, start_c)
            path = []
            path_set = {}  # cell -> index in path
            
            r, c = start_r, start_c
            
            while True:
                if r < 0 or r >= n or c < 0 or c >= n:
                    # Out of bounds - all cells in path are unsafe
                    for pr, pc in path:
                        state[pr][pc] = 3
                    break
                
                if state[r][c] == 2:
                    # Safe - all cells in path are safe
                    for pr, pc in path:
                        state[pr][pc] = 2
                        safe_count += 1
                    break
                
                if state[r][c] == 3:
                    # Unsafe - all cells in path are unsafe
                    for pr, pc in path:
                        state[pr][pc] = 3
                    break
                
                if (r, c) in path_set:
                    # Found a cycle
                    cycle_start_idx = path_set[(r, c)]
                    # All cells from cycle_start_idx onwards are in cycle -> safe
                    # All cells before cycle_start_idx lead to cycle -> safe
                    for pr, pc in path:
                        state[pr][pc] = 2
                        safe_count += 1
                    break
                
                # state[r][c] == 0, unvisited
                path_set[(r, c)] = len(path)
                path.append((r, c))
                
                dr, dc = dir_map[grid[r][c]]
                r, c = r + dr, c + dc
    
    print(safe_count)

solve()