import sys
input = sys.stdin.readline

def main():
    M, N = map(int, input().split())
    grid = []
    for _ in range(M):
        grid.append(input().strip())
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    count = 0
    
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '#':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= M or nj < 0 or nj >= N:
                        count += 1
                        break
                    elif grid[ni][nj] == '.':
                        count += 1
                        break
    
    print(count)

main()