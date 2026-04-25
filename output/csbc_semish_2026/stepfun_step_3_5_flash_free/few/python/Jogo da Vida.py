import sys

data = sys.stdin.read().split()
if not data:
    exit()
N = int(data[0])
Q = int(data[1])
grid = []
idx = 2
for i in range(N):
    linha = data[idx]
    idx += 1
    grid.append([1 if c == '1' else 0 for c in linha])

dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

for _ in range(Q):
    new_grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            for dx, dy in dirs:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < N and 0 <= nj < N:
                    cnt += grid[ni][nj]
            if grid[i][j] == 1:
                new_grid[i][j] = 1 if cnt == 2 or cnt == 3 else 0
            else:
                new_grid[i][j] = 1 if cnt == 3 else 0
    grid = new_grid

for row in grid:
    print(''.join('1' if x else '0' for x in row))