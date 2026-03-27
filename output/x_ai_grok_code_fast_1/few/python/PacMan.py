import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
grid = []
idx = 1
for i in range(N):
    grid.append(list(input_data[idx]))
    idx += 1

comida = 0
max_comida = 0
for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            cell = grid[i][j]
            if cell == 'o':
                comida += 1
            elif cell == 'A':
                comida = 0
            max_comida = max(max_comida, comida)
    else:
        for j in range(N-1, -1, -1):
            cell = grid[i][j]
            if cell == 'o':
                comida += 1
            elif cell == 'A':
                comida = 0
            max_comida = max(max_comida, comida)

print(max_comida)