
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    N, Q = map(int, data[0].split())
    grid = []
    for i in range(1, N+1):
        grid.append(list(data[i].strip()))
    
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0),  (1,1)]
    
    for _ in range(Q):
        new_grid = [['0'] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                live_neighbors = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if grid[ni][nj] == '1':
                            live_neighbors += 1
                if grid[i][j] == '1':
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[i][j] = '0'
                    else:
                        new_grid[i][j] = '1'
                else:
                    if live_neighbors == 3:
                        new_grid[i][j] = '1'
                    else:
                        new_grid[i][j] = '0'
        grid = new_grid
    
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()
