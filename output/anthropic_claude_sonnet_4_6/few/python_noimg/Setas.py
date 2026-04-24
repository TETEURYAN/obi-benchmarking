import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = []
    for i in range(n):
        grid.append(data[1 + i])
    
    # State: 0 = unknown, 1 = safe, 2 = unsafe
    state = [[0] * n for _ in range(n)]
    
    dir_map = {
        'V': (1, 0),
        'A': (-1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    
    for start_r in range(n):
        for start_c in range(n):
            if state[start_r][start_c] != 0:
                continue
            
            # Trace the path from this cell
            path = []
            visited_in_path = {}
            r, c = start_r, start_c
            
            while True:
                if r < 0 or r >= n or c < 0 or c >= n:
                    # Unsafe - all cells in path are unsafe
                    for pr, pc in path:
                        state[pr][pc] = 2
                    break
                
                if state[r][c] != 0:
                    # Already determined
                    result = state[r][c]
                    for pr, pc in path:
                        state[pr][pc] = result
                    break
                
                if (r, c) in visited_in_path:
                    # Found a cycle - all cells in cycle and path are safe
                    for pr, pc in path:
                        state[pr][pc] = 1
                    break
                
                visited_in_path[(r, c)] = len(path)
                path.append((r, c))
                
                dr, dc = dir_map[grid[r][c]]
                r += dr
                c += dc
    
    count = sum(state[r][c] == 1 for r in range(n) for c in range(n))
    print(count)

solve()