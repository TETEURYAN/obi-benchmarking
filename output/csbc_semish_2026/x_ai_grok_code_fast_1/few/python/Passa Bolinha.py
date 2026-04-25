import sys
sys.setrecursionlimit(200000)
input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx]); idx += 1
I = int(input_data[idx]) - 1; idx += 1
J = int(input_data[idx]) - 1; idx += 1
grid = []
for _ in range(N):
    row = []
    for _ in range(N):
        row.append(int(input_data[idx]))
        idx += 1
    grid.append(row)
flag = [[False] * N for _ in range(N)]
count = 0
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def process(i, j):
    global count
    if not flag[i][j]:
        flag[i][j] = True
        count += 1
    d = 0
    for _ in range(4):
        d = (d + 1) % 4
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] >= grid[i][j] and not flag[ni][nj]:
            process(ni, nj)
process(I, J)
print(count)