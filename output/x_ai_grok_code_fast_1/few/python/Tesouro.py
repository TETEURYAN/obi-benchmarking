import sys

input_data = sys.stdin.read().splitlines()
M = int(input_data[0])
grid = input_data[1:1+M]
A, B = map(int, input_data[1+M].split())
A -= 1
B -= 1

tx, ty = -1, -1
for i in range(M):
    for j in range(M):
        if grid[i][j] == 'X':
            tx, ty = i, j
            break

visited = set()
current = (A, B)
time = 0
while True:
    if current == (tx, ty):
        print(time)
        break
    if current[0] < 0 or current[0] >= M or current[1] < 0 or current[1] >= M:
        print(-1)
        break
    if current in visited:
        print(0)
        break
    visited.add(current)
    dir = grid[current[0]][current[1]]
    if dir == 'N':
        next_pos = (current[0] - 1, current[1])
    elif dir == 'S':
        next_pos = (current[0] + 1, current[1])
    elif dir == 'L':
        next_pos = (current[0], current[1] + 1)
    elif dir == 'O':
        next_pos = (current[0], current[1] - 1)
    current = next_pos
    time += 1