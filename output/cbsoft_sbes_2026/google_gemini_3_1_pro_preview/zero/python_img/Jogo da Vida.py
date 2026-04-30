import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    Q = int(input_data[1])
    
    grid = [[int(c) for c in s] for s in input_data[2:2+N]]
    
    for _ in range(Q):
        new_grid = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                alive_neighbors = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < N and 0 <= nj < N:
                            alive_neighbors += grid[ni][nj]
                
                if grid[i][j]:
                    new_grid[i][j] = 1 if alive_neighbors in (2, 3) else 0
                else:
                    new_grid[i][j] = 1 if alive_neighbors == 3 else 0
        grid = new_grid
        
    for row in grid:
        print("".join(map(str, row)))

if __name__ == '__main__':
    main()