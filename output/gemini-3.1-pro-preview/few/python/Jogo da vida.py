import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    grid = []
    for i in range(N):
        grid.append([int(x) for x in input_data[2+i]])
        
    for _ in range(Q):
        new_grid = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                count = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            count += grid[nr][nc]
                
                if grid[r][c] == 1:
                    if count == 2 or count == 3:
                        new_grid[r][c] = 1
                else:
                    if count == 3:
                        new_grid[r][c] = 1
        grid = new_grid
        
    for row in grid:
        print("".join(map(str, row)))

if __name__ == '__main__':
    main()