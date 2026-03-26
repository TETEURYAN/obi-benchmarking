
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    M = int(data[0])
    grid = []
    idx = 1
    for _ in range(M):
        grid.append(data[idx])
        idx += 1
    
    A = int(data[idx])
    B = int(data[idx + 1])
    
    r, c = A - 1, B - 1
    
    visited = [[False] * M for _ in range(M)]
    time = 0
    
    while True:
        if r < 0 or r >= M or c < 0 or c >= M:
            print(-1)
            return
        
        if visited[r][c]:
            print(0)
            return
        
        if grid[r][c] == 'X':
            print(time)
            return
        
        visited[r][c] = True
        
        direction = grid[r][c]
        if direction == 'N':
            r -= 1
        elif direction == 'S':
            r += 1
        elif direction == 'L':
            c += 1
        elif direction == 'O':
            c -= 1
        
        time += 1

solve()
