import sys

def step(grid, N):
    new_grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            neighbors = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        neighbors += grid[i+di][j+dj]
            if grid[i][j] == 0:
                if neighbors == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            else:
                if neighbors == 2 or neighbors == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
    return new_grid

def main():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    grid = []
    for i in range(N):
        row = [int(c) for c in input_data[2+i]]
        grid.append(row)
    
    for _ in range(Q):
        grid = step(grid, N)
    
    for row in grid:
        print(''.join(map(str, row)))

main()