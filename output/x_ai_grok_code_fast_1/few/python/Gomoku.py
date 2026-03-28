import sys

input_data = sys.stdin.read().split()
grid = []
for i in range(15):
    row = [int(input_data[i*15 + j]) for j in range(15)]
    grid.append(row)

dirs = [(0, 1), (1, 0), (1, 1), (1, -1)]

winner = 0
for i in range(15):
    for j in range(15):
        if grid[i][j] != 0:
            p = grid[i][j]
            for di, dj in dirs:
                count = 1
                ni, nj = i + di, j + dj
                while 0 <= ni < 15 and 0 <= nj < 15 and grid[ni][nj] == p:
                    count += 1
                    ni += di
                    nj += dj
                if count >= 5:
                    winner = p
                    break
            if winner != 0:
                break
    if winner != 0:
        break

print(winner)