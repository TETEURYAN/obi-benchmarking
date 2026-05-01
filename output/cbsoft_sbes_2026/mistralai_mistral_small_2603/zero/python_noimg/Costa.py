
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    M, N = map(int, data[0].split())
    grid = []
    for i in range(1, M + 1):
        grid.append(data[i].strip())
    
    coast = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '#':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= M or nj < 0 or nj >= N:
                        coast += 1
                    elif grid[ni][nj] == '.':
                        coast += 1
    print(coast)

if __name__ == "__main__":
    main()
