import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

M = int(input_data[0])
grid = input_data[1:M+1]
r = int(input_data[M+1]) - 1
c = int(input_data[M+2]) - 1

visited = [[False] * M for _ in range(M)]

steps = 0
while True:
    if r < 0 or r >= M or c < 0 or c >= M:
        print("-1")
        break
    
    cell = grid[r][c]
    if cell == 'X':
        print(steps)
        break
        
    if visited[r][c]:
        print("0")
        break
        
    visited[r][c] = True
    
    if cell == 'N':
        r -= 1
    elif cell == 'S':
        r += 1
    elif cell == 'L':
        c += 1
    else:
        c -= 1
        
    steps += 1