
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    grid = [list(row) for row in input_data[2:2+N]]
    
    for _ in range(Q):
        new_grid = [['0'] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                alive_neighbors = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == '1':
                            alive_neighbors += 1
                
                if grid[r][c] == '1':
                    if alive_neighbors == 2 or alive_neighbors == 3:
                        new_grid[r][c] = '1'
                else:
                    if alive_neighbors == 3:
                        new_grid[r][c] = '1'
        grid = new_grid
        
    for row in grid:
        print("".join(row))

if __name__ == '__main__':
    solve()
