
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
                alive = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            alive += grid[ni][nj]
                
                if grid[i][j] == 1:
                    if alive == 2 or alive == 3:
                        new_grid[i][j] = 1
                else:
                    if alive == 3:
                        new_grid[i][j] = 1
        grid = new_grid
        
    for row in grid:
        print("".join(map(str, row)))

if __name__ == '__main__':
    main()
